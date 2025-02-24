import csv
from datetime import datetime


class CSVHelper:
    """
    Helper class for CSV file manipulation.
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self):
        """Reads a CSV file and returns a list of dictionaries."""
        try:
            with open(self.filepath, "r") as file:
                return list(
                    csv.DictReader(file, quoting=csv.QUOTE_NONE, escapechar="\\")
                )
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    @staticmethod
    def clean_value(value, remove_dollar=True, default="0"):
        """Cleans numeric values by removing dollar signs and handling empty values."""

        if remove_dollar and "$" in value:
            value = value.replace("$", "").strip()

        try:
            if float(value):
                return value
            else:
                return default
        except ValueError as e:
            print(e)
            return default

    @staticmethod
    def format_date(date_string):
        """Formats date into MM-DD-YYYY format."""
        try:
            if "/" in date_string:
                date_string = date_string.replace("/", "-")
                date_object = datetime.strptime(date_string, "%m-%d-%Y")
            else:
                date_object = datetime.strptime(date_string, "%Y-%m-%d")

            return date_object.strftime("%m-%d-%Y")
        except Exception:
            return "Invalid Date"
