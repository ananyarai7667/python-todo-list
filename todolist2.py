def display_menu():
    print("\nTodo List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Quit")
    return input("Enter your choice: ")

def add_task(task_list):
    task = input("Enter the task to add: ")
    task_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_list):
    task = input("Enter the task to remove: ")
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print("Task not found in the list.")

def display_tasks(task_list):
    print("\nTodo List:")
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")

def main():
    todo_list = []
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            display_tasks(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
