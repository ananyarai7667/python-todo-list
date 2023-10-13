todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to display the tasks in the to-do list
def display_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("Tasks in the to-do list:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        print("Quitting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

