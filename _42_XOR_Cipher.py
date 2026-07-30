"""Encodes/decodes text with a repeating XOR key, showing results as hex."""


def xor_bytes(data, key):
    if not key:
        raise ValueError("Key cannot be empty")

    key_bytes = key.encode('utf-8')
    return bytes(byte ^ key_bytes[i % len(key_bytes)] for i, byte in enumerate(data))


def encode_to_hex(text, key):
    data = text.encode('utf-8')
    return xor_bytes(data, key).hex()


def decode_from_hex(hex_string, key):
    data = bytes.fromhex(hex_string)
    return xor_bytes(data, key).decode('utf-8')


def main():
    print("Welcome to the XOR Cipher!")
    menu = (
        "\nChoose an option:\n"
        "  1. Encode text\n"
        "  2. Decode hex\n"
        "  exit. Quit\n"
    )

    while True:
        try:
            print(menu)
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'exit':
                print("Exiting the XOR Cipher. Goodbye!")
                break

            elif choice == '1':
                text = input("Enter text to encode: ")
                key = input("Enter key: ").strip()
                hex_result = encode_to_hex(text, key)
                print(f"Encoded (hex): {hex_result}")

            elif choice == '2':
                hex_string = input("Enter hex string to decode: ").strip()
                key = input("Enter key: ").strip()
                decoded = decode_from_hex(hex_string, key)
                print(f"Decoded text: {decoded}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Invalid input: {error}")
        except UnicodeDecodeError:
            print("Could not decode the result as text. Check that the key and hex string are correct.")


if __name__ == "__main__":
    main()
