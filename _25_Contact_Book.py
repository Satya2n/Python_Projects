"""In-memory contact book: add, list, search, and delete contacts by name."""


def add_contact(contacts, name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})


def list_contacts(contacts):
    if not contacts:
        print("Your contact book is empty.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contacts(contacts, query):
    query = query.lower()
    return [c for c in contacts if query in c['name'].lower()]


def delete_contact(contacts, name):
    name = name.lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            contacts.pop(i)
            return True
    return False


def main():
    print("Welcome to the Contact Book!")
    print("Commands: add, list, search, delete, exit")
    contacts = []

    while True:
        try:
            command = input("Enter command: ").strip().lower()

            if command == 'exit':
                print("Exiting the contact book. Goodbye!")
                break

            elif command == 'add':
                name = input("Enter name: ").strip()
                phone = input("Enter phone: ").strip()
                email = input("Enter email: ").strip()
                if name:
                    add_contact(contacts, name, phone, email)
                    print("Contact added.")
                else:
                    print("Name cannot be empty.")

            elif command == 'list':
                list_contacts(contacts)

            elif command == 'search':
                query = input("Enter name to search: ").strip()
                results = search_contacts(contacts, query)
                if results:
                    for contact in results:
                        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
                else:
                    print("No matching contacts found.")

            elif command == 'delete':
                name = input("Enter name to delete: ").strip()
                if delete_contact(contacts, name):
                    print("Contact deleted.")
                else:
                    print("No contact found with that name.")

            else:
                print("Unknown command. Use: add, list, search, delete, exit")

        except (ValueError, KeyboardInterrupt):
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    main()
