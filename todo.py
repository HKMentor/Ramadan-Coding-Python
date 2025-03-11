
# To-Do List CLI (Interactive Mode) – Samjhaya Gaya
# Yeh program ek interactive CLI (Command Line Interface) hai jo To-Do List manage karne ke liye use hota hai. Aap ismein tasks add, list, complete, aur remove kar sakti hain bina baar baar python todo.py run kiye.

import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from the JSON file, or return an empty list if the file doesn't exist"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)



# 📌 Yeh function user se input leta hai aur us task ko list mein add kar deta hai.

# Har task ke saath ek done: False attribute hota hai, jo batata hai ke task complete nahi hua.

def add_task():
    """Add a new task to the todo list"""
    task = input("Enter your task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")


# 📌 Yeh function tasks ko list format mein display karta hai.

# ✅ (Green Tick) ka matlab completed task hai.
# ❌ (Cross Mark) ka matlab pending task hai.
def list_tasks():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{index}. {task['task']} [{status}]")

# 📌 Yeh function kisi bhi task ko completed mark karta hai.

# User se task number input leta hai.
# Agar valid task number hai to usko ✅ mark kar deta hai.

def complete_task():
    """Mark a task as completed"""
    list_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks = load_tasks()
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            print(f"✅ Task {task_number} marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


#  Yeh function kisi bhi task ko delete karne ke liye hai.

# User ek task number enter karega, aur woh task remove ho jayega.
def remove_task():
    """Remove a task from the list"""
    list_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        tasks = load_tasks()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed task: {removed_task['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


# 📌 Yeh function ek loop hai jo tab tak chalta rahega jab tak user 5 (Exit) nahi select karta.

# User 1 se 5 tak ka option select karega.
# Har option ek specific function ko execute karega.
# Agar user 5 select karega, toh program exit ho jayega.
def main():
    """Interactive CLI Menu"""
    while True:
        print("\n📌 To-Do List Menu:")
        print("1️⃣ Add a Task")
        print("2️⃣ List Tasks")
        print("3️⃣ Complete a Task")
        print("4️⃣ Remove a Task")
        print("5️⃣ Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    
    
#      Isko Kaise Run Karein?
# Terminal ya Command Prompt Open karein.
# python todo.py likh ke enter karein.

# 🎯 Key Benefits
# ✅ Ek hi baar run karna hota hai
# ✅ Bar bar python todo.py likhne ki zaroorat nahi
# ✅ Easy-to-use interactive menu
# ✅ File-based storage (Tasks save rahenge)
# ✅ Simple aur fast execution