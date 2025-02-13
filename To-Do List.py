tasks = []

def classify_input(user_input):
    if user_input == "1":
        new_task = input("Enter the task: ").strip()
        if new_task:
            tasks.append({"task": new_task, "completed": False})
            print(f"✅ Task '{new_task}' added!")
        else:
            print("Task cannot be an empty string.")

    elif user_input == "2":
        if not tasks:
            print("\n📌 No tasks in your list!\n")
        else:
            print("\n📌 Your To-Do List:")
            print("-" * 40)
            for index, task in enumerate(tasks, 1):
                status = "✅" if task["completed"] else "❌"
                print(f"[{index}] {status} {task['task']}")
            print("-" * 40)

    elif user_input == "3":
        completed_task = int(input("Enter the task number to mark as complete: ")) - 1
        if completed_task + 1 <= len(tasks) and completed_task >= 0:
            tasks[completed_task]["completed"] = True
            print(f"✅ '{tasks[completed_task]['task']} marked as completed!'")
        else:
            print("Invalid task number!")

    elif user_input == "4":
        remove_task = int(input("Enter the task number to remove: ")) - 1
        if remove_task + 1 <= len(tasks) and remove_task >= 0:
            del_task = tasks.pop(remove_task)
            print(f"🗑️ Task '{del_task['task']} removed!'")
        else:
            print("Invalid task number!")

    else:
        print("Invalid choice! You must enter a number between 1 and 5.")


def main():
    while True:
        print("\n📌 Welcome to Your To-Do List!\n" + "-" * 40)
        print("1️⃣  Add a new task")
        print("2️⃣  View tasks")
        print("3️⃣  Mark task as completed")
        print("4️⃣  Remove a task")
        print("5️⃣  Exit")
        print("-" * 40)

        user_input = input("Enter your choice: ")

        if user_input == "5":
            break

        classify_input(user_input)

if __name__ == "__main__":
    main()