FILENAME = "tasks.txt"

def load_tasks():
    """Loading means Reading tasks that were previously saved in a file (like tasks.txt) and bringing them back into
    your Python program as a list so the user can view, update, or delete them."""
    try:
        with open(FILENAME, "r") as file:
            """we will open the file and read("r") the file Then
            "as file" - stores the opened file in a variable called file, so you can access the file content using file
            with - ensures that the file is automatically closed after this block runs(even if there's an error)"""
            tasks = [line.strip() for line in file.readlines()]
            """file.readlines() — reads all lines in the file and returns a list of lines
            line.strip()-removes the newline characters (\n) and extra spaces from each line
            for line in file.readlines() — for each line in the file"""
    except FileNotFoundError: #If the file you’re trying to read (FILENAME) is not found, Python raises a FileNotFoundError
        tasks = []
        """If the file isn't found, we assume there are no tasks yet, so we create an empty list
        This avoids an error and lets your program continue running"""
    return tasks #If file was found, it returns all tasks from the file.If file wasn’t found, it returns an empty list.

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        """We will open the file and write("w")the file
        write("w")-If the file doesn’t exist, it will be created.If the file already exists, it will be overwritten (old content is erased).
        then with(automatically closes file after we are done writing)"""
        for task in tasks:
            file.write(task + "\n")
            # If tasks = ["Buy groceries", "Finish homework", "Call mom"],Then all three printed in three lines(because of \n)

def show_menu():
    print("\n _____ TO-DO LIST MENU _____")
    print("\n 1. View Task ")
    print("\n 2. Add Task ")
    print("\n 3. Remove Task")
    print("\n 4. Exit")
    
def view_task(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added and saved.")
    
def remove_task(tasks):
    view_task(tasks)
    try:
        index = int(input("Enter the Task Number to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1) # Why index - 1 Because Python lists start at 0. So Task 1 → index 0, Task 2 → index 1
            save_tasks(tasks)
            print(f"Removed task: {removed_task}")
        else:
            print(f"No Task Found ")
        
    except ValueError:
        print("Please enter a valid number.")
        
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter Your Choice (1/2/3/4): ")
        
        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Tasks saved. Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()
            
            


