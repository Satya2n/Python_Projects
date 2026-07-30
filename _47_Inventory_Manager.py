"""In-memory inventory manager: add, update, remove items and track total value."""


def add_item(inventory, name, quantity, price):
    inventory[name] = {'quantity': quantity, 'price': price}


def list_items(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    for name, details in inventory.items():
        item_total = details['quantity'] * details['price']
        print(f"{name}: qty {details['quantity']} @ ${details['price']:.2f} = ${item_total:.2f}")


def update_quantity(inventory, name, quantity):
    if name in inventory:
        inventory[name]['quantity'] = quantity
        return True
    return False


def remove_item(inventory, name):
    if name in inventory:
        del inventory[name]
        return True
    return False


def total_inventory_value(inventory):
    return sum(details['quantity'] * details['price'] for details in inventory.values())


def main():
    print("Welcome to the Inventory Manager!")
    print("Commands: add, list, update, remove, total, exit")
    inventory = {}

    while True:
        try:
            command = input("Enter command: ").strip().lower()

            if command == 'exit':
                print("Exiting the Inventory Manager. Goodbye!")
                break

            elif command == 'add':
                name = input("Enter item name: ").strip()
                quantity = int(input("Enter quantity: ").strip())
                price = float(input("Enter price per unit: ").strip())
                if not name:
                    print("Item name cannot be empty.")
                    continue
                add_item(inventory, name, quantity, price)
                print("Item added.")

            elif command == 'list':
                list_items(inventory)

            elif command == 'update':
                name = input("Enter item name to update: ").strip()
                quantity = int(input("Enter new quantity: ").strip())
                if update_quantity(inventory, name, quantity):
                    print("Quantity updated.")
                else:
                    print("Item not found.")

            elif command == 'remove':
                name = input("Enter item name to remove: ").strip()
                if remove_item(inventory, name):
                    print("Item removed.")
                else:
                    print("Item not found.")

            elif command == 'total':
                print(f"Total inventory value: ${total_inventory_value(inventory):.2f}")

            else:
                print("Unknown command. Use: add, list, update, remove, total, exit")

        except ValueError:
            print("Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main()
