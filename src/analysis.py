import sys

from utils import CSVHelper
import requests
import os
from dotenv import load_dotenv


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
        "potential_gain",
    ]

    data_quality_paragraph = """\
The following quality issues were found in the CSV file:
- product_name had wrapping '' marks
- our_price formatting was inconsistent ($ sign was not always included)
- current_stock and restock_threshold had empty values
- Dates were not standardized
"""

    cleanup_paragraph = """\
The following cleanup was performed:
- Capitalized product_name and removed wrapping '' marks
- Standardized our_price by removing $ sign
- Capitalized category
- Replaced empty values with 0
- Formatted dates uniformly (mm-dd-yyyy)
"""

    future_recommendations = """\
To maximize potential earnings, restocking items when quantity dips to the restock threshold
can help maintain inventory. Analyzing month-to-month sales can also help adjust thresholds effectively.
"""

    try:
        with open(markdown_filepath, "w", newline="") as mdfile:
            mdfile.write(data_quality_paragraph + "\n")
            mdfile.write(cleanup_paragraph + "\n")
            mdfile.write("\n## Cleaned Data Summary\n")

            mdfile.write("| " + " | ".join(headers) + " |\n")
            mdfile.write("| " + " | ".join(["---"] * len(headers)) + " |\n")

            potential_total = 0.0
            total_prices = 0.0
            valid_price_count = 0
            total_stock = 0

            for row in rows:
                # Grab date before cleaning row
                date_string = list(
                    {k: v for k, v in row.items() if k is None}.values()
                )[0][0]

                # Clean row
                row = {k: v for k, v in row.items() if k}

                # Clean row values
                row["date"] = csv_helper.format_date(date_string)
                row["our_price"] = csv_helper.clean_value(row.get("our_price", "0"))
                row["current_stock"] = csv_helper.clean_value(
                    row.get("current_stock", "0")
                )
                row["restock_threshold"] = csv_helper.clean_value(
                    row.get("restock_threshold", "0")
                )
                row["product_name"] = (
                    row.get("product_name", "").replace('"', "").capitalize()
                )
                row["category"] = row.get("category", "").capitalize()

                # Convert price and stock to numerical values
                our_price = float(row["our_price"]) if row["our_price"] else 0.0
                current_stock = (
                    int(row["current_stock"]) if row["current_stock"].isdigit() else 0
                )

                # Calculate potential gain
                row["potential_gain"] = str(our_price * current_stock)
                potential_total += our_price * current_stock
                total_stock += current_stock

                if our_price > 0:
                    total_prices += our_price
                    valid_price_count += 1

                # Write to report.md
                mdfile.write(
                    "| " + " | ".join(row.get(h, "") for h in headers) + " |\n"
                )

            # Load environment variables from the .env file
            load_dotenv()

            # RapidAPI grocery Prices
            def get_external_price(query):
                url = os.getenv("API_URL")
                querystring = {"keyword": query, "perPage": "10", "page": "1"}
                headers = {
                    "x-rapidapi-key": os.getenv("API_KEY"),
                    "x-rapidapi-host": os.getenv("API_HOST"),
                }

                response = requests.get(url, headers=headers, params=querystring)
                json_data = (
                    response.json()
                    if response and response.status_code == 200
                    else None
                )

                if "hits" in json_data and isinstance(json_data["hits"], list):
                    external_price = (
                        json_data["hits"][0]["priceInfo"]["linePrice"]
                        .replace("$", "")
                        .strip()
                    )
                    return external_price
                else:
                    return "Not found"

            def calculate_percentage(num1, num2):
                if float(num2) == 0:
                    return None
                return f"{abs(num1 - num2) / ((num1 + num2) / 2) * 100:.2f}%"

            avg_price_per_item = round((total_prices / len(rows)), 2)
            avg_items_in_stock = round((total_stock / len(rows)), 2)
            external_price = get_external_price("coffee")

            # Write insights and future recommendations
            mdfile.write("\n## Insights\n")
            mdfile.write(f"\n**Potential Total Earnings:** ${potential_total:.2f}\n")
            mdfile.write(f"\n**Average Price per Item:** ${avg_price_per_item:.2f}\n")
            mdfile.write(
                f"\n**Average number of items in stock:** {round(avg_items_in_stock)}\n"
            )
            mdfile.write(
                f"\n**Potential Earnings (assuming missing prices are average):** ${potential_total + (avg_price_per_item * avg_items_in_stock):.2f}\n"
            )
            mdfile.write(
                f"\n**Deficit (Missing prices impact):** ${potential_total + (avg_price_per_item * round(avg_items_in_stock)) - potential_total:.2f}\n"
            )
            mdfile.write("\n## Future Recommendations\n")
            mdfile.write(f"\n{future_recommendations}\n")
            mdfile.write(
                "Accurately setting prices is crucial to calculating earnings. Missing prices skew projections.\n"
            )
            mdfile.write(
                "\nDue to rate limiting and free tier of RapidAPI (external price data) limitations. The following example references coffee.\n"
            )
            mdfile.write(
                f"\nThe price for an external source is **${external_price}**.\n"
            )
            mdfile.write("\nOur price is **$14.99**.\n")
            mdfile.write(
                f"\nThe percentage difference between our price and the external price is **{calculate_percentage(14.99, float(external_price))}**. Meaning there is a significant profit being made assuming quantity and weight are the same.\n"
            )
    except Exception as e:
        print(f"An error occurred while writing Markdown: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_csv_file = sys.argv[1]
        output_file = "report.md"
        csv_to_markdown_table(input_csv_file, output_file)
    else:
        print("Please provide an input csv file.")
