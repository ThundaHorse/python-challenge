import sys
from utils import CSVHelper
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def csv_to_markdown_table(csv_filepath, markdown_filepath):
    """Converts a CSV file into a Markdown table."""
    csv_helper = CSVHelper(csv_filepath)
    rows = csv_helper.read_csv()
    headers = [
        "product_name",
        "our_price",
        "category",
        "current_stock",
        "restock_threshold",
        "date",
    ]

    try:
        with open(markdown_filepath, "w", newline="") as mdfile:
            data_quality_paragraph = """The following quality issues were found in the CSV file
            - product_name had wrapping '' marks
            - our_price as formatting of pricing was not consistent ($ were included in not all)
            - current_stock and restock_threshold had empty values
            - Dates were not standardized
            """
            cleanup_paragrah = """The following clean up was performed:
            - Capitalize product_name, remove wrapping '' marks
            - Standardized display for our_price by removing $ sign
            - Capitalized category
            - For values that were empty, by default added ??? placeholder
            - Formatted dates to be uniform (mm-dd-yyy)"""

            mdfile.write(data_quality_paragraph + "\n")
            mdfile.write(cleanup_paragrah + "\n")
            mdfile.write("\nCleaned up Data Summary\n")

            mdfile.write("| " + " | ".join(headers) + " |\n")
            mdfile.write("| " + " | ".join(["---"] * len(headers)) + " |\n")

            for row in rows:
                """Grab date before cleaning row"""
                date_string = list(
                    {k: v for k, v in row.items() if k is None}.values()
                )[0][0]

                """Clean row"""
                row = {k: v for k, v in row.items() if k}

                """Assign values"""
                row["our_price"] = csv_helper.clean_value(row.get("our_price", ""))
                row["current_stock"] = csv_helper.clean_value(
                    row.get("current_stock", "")
                )
                row["restock_threshold"] = csv_helper.clean_value(
                    row.get("restock_threshold", "")
                )
                row["product_name"] = (
                    row.get("product_name", "").replace('"', "").capitalize()
                )
                row["category"] = row.get("category", "").capitalize()
                row["date"] = csv_helper.format_date(date_string)

                """Write to report.md"""
                mdfile.write(
                    "| " + " | ".join(row.get(h, "") for h in headers) + " |\n"
                )
            mdfile.write("\n")
            mdfile.write("Insights: \n")
            mdfile.write("COMING SOON")
    except Exception as e:
        print(f"An error occurred while writing Markdown: {e}")


def get_pricing_info():
    api_url = "https://api.api-ninjas.com/v1/commodityprice?name={}".format("coffee")
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_csv_file = sys.argv[1]
        output_file = "report.md"
        csv_to_markdown_table(input_csv_file, output_file)
        get_pricing_info()
    else:
        print("Please provide an input csv file.")
