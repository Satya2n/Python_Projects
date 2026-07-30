"""In-memory expense tracker: add, list, and summarize expenses by category."""


def add_expense(expenses, description, amount, category):
    expenses.append({'description': description, 'amount': amount, 'category': category})


def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['description']} | ${expense['amount']:.2f} | {expense['category']}")


def total_spent(expenses):
    return sum(expense['amount'] for expense in expenses)


def total_by_category(expenses):
    totals = {}
    for expense in expenses:
        category = expense['category']
        totals[category] = totals.get(category, 0) + expense['amount']
    return totals


def remove_expense(expenses, index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    return None


def main():
    print("Welcome to the Expense Tracker!")
    print("Commands: add, list, total, by_category, remove, exit")
    expenses = []

    while True:
        try:
            command = input("Enter command: ").strip().lower()

            if command == 'exit':
                print("Exiting the Expense Tracker. Goodbye!")
                break

            elif command == 'add':
                description = input("Enter description: ").strip()
                amount = float(input("Enter amount: ").strip())
                category = input("Enter category: ").strip() or "Uncategorized"
                if not description:
                    print("Description cannot be empty.")
                    continue
                add_expense(expenses, description, amount, category)
                print("Expense added.")

            elif command == 'list':
                list_expenses(expenses)

            elif command == 'total':
                print(f"Total spent: ${total_spent(expenses):.2f}")

            elif command == 'by_category':
                totals = total_by_category(expenses)
                if not totals:
                    print("No expenses recorded yet.")
                else:
                    for category, amount in totals.items():
                        print(f"{category}: ${amount:.2f}")

            elif command == 'remove':
                list_expenses(expenses)
                index = int(input("Enter the number of the expense to remove: ").strip()) - 1
                removed = remove_expense(expenses, index)
                if removed:
                    print(f"Removed: {removed['description']}")
                else:
                    print("Invalid expense number.")

            else:
                print("Unknown command. Use: add, list, total, by_category, remove, exit")

        except ValueError:
            print("Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main()
