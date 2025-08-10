import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    deadline = input("Deadline (YYYY-MM-DD): ")
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return
    tasks = load_tasks()
    tasks.append({"task": task, "priority": priority, "deadline": deadline, "completed": False})
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("⚠ No tasks found.")
        return

    print(f"{'No.':<4}{'Task':<20}{'Priority':<10}{'Deadline':<12}{'Status'}")
    for i, t in enumerate(tasks, 1):
        status = "✅ Done" if t["completed"] else "❌ Pending"
        print(f"{i:<4}{t['task']:<20}{t['priority']:<10}{t['deadline']:<12}{status}")

def complete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as complete: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    tasks = load_tasks()
    if 1 <= num <= len(tasks):
        tasks[num-1]["completed"] = True
        save_tasks(tasks)
        print("🎯 Task marked completed!")
    else:
        print("❌ Invalid number.")

def menu():
    while True:
        print("\n=== 📋 To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
