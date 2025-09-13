tasks = []
def show_tasks():
  if not tasks: print(" No tasks yet.")
  else:
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")
def add_task(task):
  tasks.append(task)
  print(f"Task added: {task}")
def remove_task(index):
  try: removed = tasks.pop(index - 1)
  print(f"Task removed: {removed}")
  except IndexError: print(" Invalid task number.")
if name == "main":
  while True: print("\n--- To-Do List ---")
    print("1. Show tasks\n2. Add task\n3. Remove task\n4. Exit")
choice = input("Choose: ")
