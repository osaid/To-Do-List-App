import csv

FILENAME = "TaskList.csv"


def add_Task():
    print("Add Tasks\n")
    addTaskOptions = int(input("1.Add New Task\n2.Return to menu\n"))
    if addTaskOptions == 1:
        task = input("Enter a new task: ")
        status = "Not Started"  # Default status for new tasks

        # Read existing tasks to determine the next ID
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                rows = [row for row in reader if row]  # Skip empty rows
                if len(rows) == 0:  # File is empty, start with ID 1
                    new_id = 1
                    # Write header if it's a brand new file
                    with open(FILENAME, "w", newline="") as file_write:
                        writer = csv.writer(file_write)
                        writer.writerow(["ID", "Task", "Status"])
                else:
                    # If header exists, subtract 1 to get actual number of tasks
                    new_id = len(rows) if rows[0][0] != "ID" else len(rows)
        except FileNotFoundError:
            # If file doesn't exist, create it and write header
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Task", "Status"])
            new_id = 1

        # Append the new task with ID and status
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, task, status])

        print(f"Task added: {new_id} - {task} - {status}")

    elif addTaskOptions == 2:
        return
    else:
        print("Invalid Option")
        return


def view_Task():
    print("View Tasks\n")
    viewTaskOptions = int(input("1.View All Tasks\n2.Return to menu\n"))

    if viewTaskOptions == 1:
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [row for row in reader if row]  # Skip empty rows

                if len(tasks) <= 1:  # Only header or empty
                    print("No tasks found.")
                    return

                header = tasks[0]
                data_rows = tasks[1:]  # Exclude header

                # Upgrade old tasks that have only ID and Task
                for row in data_rows:
                    if len(row) < 3:  # Status missing
                        row.append("Not Started")

                # Print tasks
                for task in data_rows:
                    print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.")

    elif viewTaskOptions == 2:
        return
    else:
        print("Invalid Option")
        return


def complete_Task():  # This function displays all the tasks and asks the user to input 1 if they want to input the ID of the task they want to mark as complete or 2 to return to the menu
    print("You're On Complete Tasks")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader if row]  # Skip empty rows

            if len(tasks) <= 1:  # Only header or empty
                print("No tasks found.")
                return

            header = tasks[0]
            data_rows = tasks[1:]  # Exclude header

            # Print tasks
            for task in data_rows:
                print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")
        return

    completeTaskOptions = int(input("1.Complete Task\n2.Return to menu\n"))
    if completeTaskOptions == 1:


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
