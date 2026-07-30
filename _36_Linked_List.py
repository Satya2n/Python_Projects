"""Implements a singly linked list from scratch with an interactive menu to exercise it."""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def find(self, data):
        current = self.head
        index = 0

        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def to_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def display(self):
        if self.head is None:
            return "(empty list)"
        return " -> ".join(str(item) for item in self.to_list())


def main():
    linked_list = LinkedList()
    print("Welcome to the Linked List demo!")
    menu = (
        "\nChoose an option:\n"
        "  1. Append value\n"
        "  2. Prepend value\n"
        "  3. Delete value\n"
        "  4. Find value\n"
        "  5. Display list\n"
        "  exit. Quit\n"
    )

    while True:
        try:
            print(menu)
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'exit':
                print("Exiting the Linked List demo. Goodbye!")
                break

            elif choice == '1':
                value = input("Enter value to append: ").strip()
                linked_list.append(value)
                print(f"Appended '{value}'. List: {linked_list.display()}")

            elif choice == '2':
                value = input("Enter value to prepend: ").strip()
                linked_list.prepend(value)
                print(f"Prepended '{value}'. List: {linked_list.display()}")

            elif choice == '3':
                value = input("Enter value to delete: ").strip()
                if linked_list.delete(value):
                    print(f"Deleted '{value}'. List: {linked_list.display()}")
                else:
                    print(f"'{value}' not found in the list.")

            elif choice == '4':
                value = input("Enter value to find: ").strip()
                index = linked_list.find(value)
                if index == -1:
                    print(f"'{value}' not found in the list.")
                else:
                    print(f"'{value}' found at index {index}.")

            elif choice == '5':
                print(f"List: {linked_list.display()}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
