"""Validates and pretty-prints user-entered JSON, reporting parse errors with location."""

import json


def read_json_input():
    print("Enter your JSON, line by line (type 'END' when finished, or 'exit' to quit the program):")
    lines = []
    while True:
        line = input()
        stripped = line.strip()

        if stripped.lower() == 'exit' and not lines:
            return None

        if stripped == 'END':
            break

        lines.append(line)

    return "\n".join(lines)


def pretty_print_json(text):
    data = json.loads(text)
    return json.dumps(data, indent=4, sort_keys=True)


def main():
    print("Welcome to the JSON Pretty Printer!")
    while True:
        try:
            raw = read_json_input()

            if raw is None:
                print("Exiting the JSON Pretty Printer. Goodbye!")
                break

            if not raw.strip():
                print("No JSON was entered. Please try again.")
                continue

            pretty = pretty_print_json(raw)
            print("Valid JSON! Pretty-printed result:")
            print(pretty)

        except json.JSONDecodeError as error:
            print(
                f"Invalid JSON: {error.msg} at line {error.lineno}, "
                f"column {error.colno} (char {error.pos})."
            )
        except Exception:
            print("Something went wrong while processing that input. Please try again.")


if __name__ == "__main__":
    main()
