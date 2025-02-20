import csv
import sys
from datetime import datetime
import re


def csv_to_markdown_table(csv_filepath, markdown_filepath):
    """
    Convert desired CSV file to Markdown table and save it to a report.md.

    Args:
        csv_filepath (str): The path to the input CSV file.
        markdown_filepath (str): The path to the output Markdown file.
    """

    # Error Handling
    try:
        with (
            open(csv_filepath, "r") as csvfile,
            open(markdown_filepath, "w", newline="") as mdfile,
        ):
            # Set reader to read from dict
            # Handle cases where csv is not properly delimited
            # i.e. Rooibos Tea was not properly delimited
            reader = csv.DictReader(csvfile, quoting=csv.QUOTE_NONE, escapechar="\\")

            # Extract headers
            # Set desired information
            headers = [
                "product_name",
                "our_price",
                "category",
                "current_stock",
                "restock_threshold",
                "date",
            ]

            # Set initial Row
            mdfile.write("| " + " | ".join(headers) + " |\n")
            mdfile.write("| " + " | ".join(["---"] * len(headers)) + " |\n")

            for row in reader:
                cleaned_row = {k: v for k, v in row.items() if k is not None}

                try:
                    date_string = list(
                        {k: v for k, v in row.items() if k is None}.values()
                    )[0][0]

                    # Clean up formatting for our_price, current_stock, and restock_threshold if no value & remove dollar sign if present
                    cleaned_row["our_price"] = (
                        cleaned_row["our_price"].replace("$", " ")
                        if "$" in cleaned_row["our_price"]
                        else cleaned_row["our_price"]
                    )
                    cleaned_row["our_price"] = (
                        "0"
                        if cleaned_row["our_price"] == ""
                        else cleaned_row["our_price"]
                    )
                    cleaned_row["current_stock"] = (
                        cleaned_row["current_stock"].replace("$", " ")
                        if "$" in cleaned_row["current_stock"]
                        else cleaned_row["current_stock"]
                    )
                    cleaned_row["current_stock"] = (
                        "0"
                        if cleaned_row["current_stock"] == ""
                        else cleaned_row["current_stock"]
                    )
                    cleaned_row["restock_threshold"] = (
                        cleaned_row["restock_threshold"].replace("$", " ")
                        if "$" in cleaned_row["restock_threshold"]
                        else cleaned_row["restock_threshold"]
                    )
                    cleaned_row["restock_threshold"] = (
                        "0"
                        if cleaned_row["restock_threshold"] == ""
                        else cleaned_row["restock_threshold"]
                    )

                    cleaned_row["product_name"] = (
                        cleaned_row["product_name"].strip('"').capitalize()
                        if "$" in cleaned_row["product_name"]
                        else cleaned_row["product_name"]
                    )
                    cleaned_row["category"] = cleaned_row["category"].capitalize()

                    # Date format error, manual fix
                    if "/" in date_string:
                        date_string = date_string.replace("/", "-")
                        date_object = datetime.strptime(date_string, "%m-%d-%Y")
                        formatted_date_string = date_object.strftime("%m-%d-%Y")
                    else:
                        date_object = datetime.strptime(date_string, "%Y-%m-%d")
                        formatted_date_string = date_object.strftime("%m-%d-%Y")

                    cleaned_row["date"] = formatted_date_string
                    mdfile.write(
                        "| " + " | ".join(cleaned_row[h] for h in headers) + " |\n"
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")

    except FileNotFoundError:
        print(f"Error: Input file '{csv_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred when parsing: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_csv_file = sys.argv[1]
        output_file = "report.md"
        csv_to_markdown_table(
            csv_filepath=input_csv_file, markdown_filepath=output_file
        )
    else:
        print("Please provide an input csv file.")
