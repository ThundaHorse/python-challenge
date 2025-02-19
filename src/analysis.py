import csv
import sys
from datetime import datetime


def copy_csv_data(input_filepath, output_filepath):
    """
    Reads data from a CSV file and writes it to a new CSV file.

    Args:
        input_filepath (str): The path to the input CSV file.
        output_filepath (str): The path to the output CSV file.
    """
    try:
        with (
            open(input_filepath, "r") as infile,
            open(output_filepath, "w", newline="") as outfile,
        ):
            fieldnames = [
                "product_name",
                "our_price",
                "category",
                "current_stock",
                "restock_threshold",
                "date",
            ]
            reader = csv.DictReader(infile)

            writer = csv.DictWriter(
                outfile, fieldnames=fieldnames, delimiter=",", extrasaction="ignore"
            )
            writer.writeheader()

            for row in reader:
                cleaned_row = {k: v for k, v in row.items() if k is not None}

                date_string = list(
                    {k: v for k, v in row.items() if k is None}.values()
                )[0][0]

                if "/" in date_string:
                    date_string = date_string.replace("/", "-")
                    date_object = datetime.strptime(date_string, "%m-%d-%Y")
                    formatted_date_string = date_object.strftime("%d/%m/%Y")
                else:
                    date_object = datetime.strptime(date_string, "%Y-%m-%d")
                    formatted_date_string = date_object.strftime("%d/%m/%Y")
                    cleaned_row["date"] = formatted_date_string
                print(cleaned_row)
                writer.writerow(cleaned_row)

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_csv_file = sys.argv[1]
        output_file = "report.md"
        copy_csv_data(input_filepath=input_csv_file, output_filepath=output_file)
    else:
        print("Please provide an input csv file.")
