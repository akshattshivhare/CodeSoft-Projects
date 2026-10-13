"""Task 3: To-Do List with persistent storage (CODSOFT Python Internship)."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks() -> list:
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: tasks.json was corrupted, starting fresh.")
    return []


def save_tasks(tasks: list) -> None:
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def show_tasks(tasks: list) -> None:
    if not tasks:
        print("\n  No tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"  {i}. [{mark}] {task['title']}")


def ask_index(tasks: list, action: str):
    show_tasks(tasks)
    if not tasks:
        return None
    try:
        idx = int(input(f"\nTask number to {action}: ")) - 1
        if 0 <= idx < len(tasks):
            return idx
    except ValueError:
        pass
    print("  Invalid task number.")
    return None


def add_task(tasks: list) -> None:
    title = input("Task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("  Task added.")
    else:
        print("  Task cannot be empty.")


def complete_task(tasks: list) -> None:
    idx = ask_index(tasks, "mark complete")
    if idx is not None:
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("  Marked as complete.")


def edit_task(tasks: list) -> None:
    idx = ask_index(tasks, "edit")
    if idx is not None:
        new_title = input("New description: ").strip()
        if new_title:
            tasks[idx]["title"] = new_title
            save_tasks(tasks)
            print("  Task updated.")


def delete_task(tasks: list) -> None:
    idx = ask_index(tasks, "delete")
    if idx is not None:
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"  Deleted: {removed['title']}")


def main() -> None:
    tasks = load_tasks()
    actions = {
        "1": ("View tasks", lambda: show_tasks(tasks)),
        "2": ("Add task", lambda: add_task(tasks)),
        "3": ("Mark task complete", lambda: complete_task(tasks)),
        "4": ("Edit task", lambda: edit_task(tasks)),
        "5": ("Delete task", lambda: delete_task(tasks)),
    }
    print("=== To-Do List ===")
    while True:
        print("\nMenu:")
        for key, (label, _) in actions.items():
            print(f"  {key}. {label}")
        print("  6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
