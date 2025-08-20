import csv

FILENAME = "TaskList.csv"  # Defined the filename for the task list


def add_Task():
    print("Add Tasks\n")
    # Option to add a new task or return to the menu
    addTaskOptions = int(input("1.Add New Task\n2.Return to menu\n"))
    if addTaskOptions == 1:  # If the user chooses to add a new task
        task = input("Enter a new task: ")
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)  # Read the CSV file
                rows = list(reader)  # Read all rows into a list
                if len(rows) == 0:  # If the file is empty, start with ID 1
                    new_id = 1
                else:
                    new_id = len(rows)  # Get the last ID and increment it by 1

        except FileNotFoundError:  # If the file does not exist, create it
            with open(FILENAME, "w", newline="") as file:  # Create the file and write the header
                writer = csv.writer(file)  # Write the header
                writer.writerow(["ID", "Task"])  # Write the header row
            new_id = 1

        with open(FILENAME, "a", newline="") as file:  # Open the file in append mode
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerow([new_id, task])  # Write the new task with its ID
        print(f"Task added: {new_id} - {task}")  # Confirmation message
    elif addTaskOptions == 2:
        return  # If the user chooses to return to the menu
    else:
        print("Invalid Option")
        return  # If the user enters an invalid option, return to add task menu


def view_Task():
    print("View Tasks\n")

    viewTaskOptions = int(input("1.View All Tasks\n2.Return to menu\n"))
    if viewTaskOptions == 1:  # If the user chooses to view all tasks
        try:
            with open(FILENAME, "r", newline="") as file:  # Open the CSV file for reading
                reader = csv.reader(file)  # Create a CSV reader object
                next(reader)  # Skip the header row
                tasks = list(reader)  # Read all tasks into a list
                if not tasks:  # If there are no tasks, print a message
                    print("No tasks found.")
                else:
                    for task in tasks:  # Iterate through each task and print it
                        print(f"ID: {task[0]}, Task: {task[1]}")
        except FileNotFoundError:  # If the file does not exist, print a message
            print("No tasks found. Please add a task first.")
    elif viewTaskOptions == 2:
        return
    else:
        print("Invalid Option")
        return


def complete_Task():
    print("You're On Complete Tasks")


def delete_Task():
    print("You're On Delete Tasks")


def menu():
    print("Welcome to Listy, your personal to-do list app")
    print("Please Select from one of the options: \n")

    while True:
        menuOptions = int(
            input("1.Add Task \n2.View Tasks\n3.Complete Tasks\n4.Delete Tasks\n5.Exit\n"))
        if menuOptions == 1:
            add_Task()
        elif menuOptions == 2:
            view_Task()
        elif menuOptions == 3:
            complete_Task()
        elif menuOptions == 4:
            delete_Task()
        elif menuOptions == 5:
            exit()
        else:
            print("Invalid Option")
            continue

        if not menuOptions:
            break


menu()
