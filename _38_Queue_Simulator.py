"""Simulates a customer/ticket queue using collections.deque as a real queue structure."""

from collections import deque


def enqueue(queue, name):
    queue.append(name)


def dequeue(queue):
    return queue.popleft() if queue else None


def main():
    queue = deque()
    print("Welcome to the Queue Simulator!")
    menu = (
        "\nChoose an option:\n"
        "  1. Enqueue (add person)\n"
        "  2. Dequeue (serve next person)\n"
        "  3. View queue\n"
        "  4. View queue length\n"
        "  exit. Quit\n"
    )

    while True:
        try:
            print(menu)
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'exit':
                print("Exiting the Queue Simulator. Goodbye!")
                break

            elif choice == '1':
                name = input("Enter the person's name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                enqueue(queue, name)
                print(f"'{name}' has been added to the queue.")

            elif choice == '2':
                served = dequeue(queue)
                if served is None:
                    print("The queue is empty. No one to serve.")
                else:
                    print(f"Now serving: '{served}'.")

            elif choice == '3':
                if not queue:
                    print("The queue is empty.")
                else:
                    print("Current queue (front to back): " + " -> ".join(queue))

            elif choice == '4':
                print(f"Queue length: {len(queue)}")

            else:
                print("Invalid choice. Please try again.")

        except Exception:
            print("Something went wrong with that input. Please try again.")


if __name__ == "__main__":
    main()
