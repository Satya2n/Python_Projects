"""In-memory to-do list manager: add, list, mark done, and remove tasks."""


def add_task(tasks, description):
    tasks.append({'description': description, 'done': False})


def list_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['done'] else "[ ]"
        print(f"{index}. {status} {task['description']}")


def mark_done(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['done'] = True
        return True
    return False


def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        return True
    return False


def main():
    print("Welcome to the To-Do List Manager!")
    print("Commands: add, list, done <index>, remove <index>, exit")
    tasks = []

    while True:
        try:
            command = input("Enter command: ").strip()

            if not command:
                continue

            lowered = command.lower()

            if lowered == 'exit':
                print("Exiting the to-do list manager. Goodbye!")
                break

            if lowered == 'add':
                description = input("Enter task description: ").strip()
                if description:
                    add_task(tasks, description)
                    print("Task added.")
                else:
                    print("Task description cannot be empty.")
                continue

            if lowered == 'list':
                list_tasks(tasks)
                continue

            parts = command.split(maxsplit=1)
            action = parts[0].lower()

            if action in ('done', 'remove') and len(parts) == 2:
                index = int(parts[1])
                if action == 'done':
                    if mark_done(tasks, index):
                        print(f"Task {index} marked as done.")
                    else:
                        print("Invalid task index.")
                else:
                    if remove_task(tasks, index):
                        print(f"Task {index} removed.")
                    else:
                        print("Invalid task index.")
                continue

            print("Unknown command. Use: add, list, done <index>, remove <index>, exit")

        except ValueError:
            print("Invalid index. Please enter a number, e.g. 'done 1'.")


if __name__ == "__main__":
    main()
