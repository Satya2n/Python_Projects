"""Converts user-entered CSV lines (header + rows) into a JSON array of objects."""

import csv
import json


def csv_lines_to_json(lines):
    reader = csv.reader(lines)
    rows = list(reader)

    if not rows:
        return "[]"

    header = rows[0]
    records = []
    for row in rows[1:]:
        record = {header[i]: (row[i] if i < len(row) else "") for i in range(len(header))}
        records.append(record)

    return json.dumps(records, indent=4)


def read_csv_input():
    print("Enter CSV lines, header row first (type 'END' when finished, or 'exit' to quit the program):")
    lines = []
    while True:
        line = input()
        stripped = line.strip()

        if stripped.lower() == 'exit' and not lines:
            return None

        if stripped == 'END':
            break

        lines.append(line)

    return lines


def main():
    print("Welcome to the CSV to JSON Converter!")
    while True:
        try:
            lines = read_csv_input()

            if lines is None:
                print("Exiting the CSV to JSON Converter. Goodbye!")
                break

            if not lines:
                print("No CSV data was entered. Please try again.")
                continue

            json_output = csv_lines_to_json(lines)
            print("Converted JSON:")
            print(json_output)

        except csv.Error:
            print("Could not parse that as CSV. Please try again.")
        except Exception:
            print("Something went wrong while processing that input. Please try again.")


if __name__ == "__main__":
    main()
