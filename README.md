# ToDoList
tasks = []
def show_tasks():
    if not tasks:
        print(" No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")
def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Task removed: {removed}")
    except IndexError:
        print(" Invalid task number.")
if __name__ == "__main__":
    while True:
        print("\n--- To-Do List ---")
        print("1. Show tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            num = int(input("Enter task number to remove: "))
            remove_task(num)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
