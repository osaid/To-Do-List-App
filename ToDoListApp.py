import csv

FILENAME = "TaskList.csv"


def add_Task():
    """
    Add a new task to the CSV file.

    Prompts the user for task details: name, due date and priority.
    Automatically assigns a unique ID and sets the status to "Not Started".
    Creates the CSV file and header if it does not exist.
    """
    print("Add Tasks\n")
    addTaskOptions = int(input("1.Add New Task\n2.Return to menu\n"))
    if addTaskOptions == 1:
        task = input("Enter a new task: ").title()
        status = "Not Started"
        dueDate = input("Please enter the due date: ")
        priority = input(
            "Please enter the priority(Low/Medium/High): ").title()

        # Determine the next available ID based on the existing CSV
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                rows = [row for row in reader if row]  # ignore blank rows
                if len(rows) == 0:  # brand new file
                    new_id = 1
                    with open(FILENAME, "w", newline="") as file_write:
                        writer = csv.writer(file_write)
                        writer.writerow(
                            ["ID", "Task", "Status", "Due Date", "Priority"])
                else:
                    new_id = len(rows) if rows[0][0] != "ID" else len(rows)
        except FileNotFoundError:
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ID", "Task", "Status", "Due Date", "Priority"])
            new_id = 1

        # Append the new task to the CSV
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, task, status, dueDate, priority])

        print(
            f"Task added: {new_id} - {task} - Status: {status} - Due Date: {dueDate} - Priority: {priority}")

    elif addTaskOptions == 2:
        return
    else:
        print("Invalid Option")
        return


def view_Task():
    """
    View and optionally edit tasks in the CSV file.

    User can:
    - View all tasks in a formatted list.
    - Edit the name of an existing task by specifying its ID.
    """
    print("View Tasks\n")
    viewTaskOptions = int(
        input("1.View All Tasks\n2.Edit Task Name\n3.Return to menu\n"))

    if viewTaskOptions == 1:
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [row for row in reader if row]

                if len(tasks) <= 1:
                    print("No tasks found. Please add a task first.\n")
                    return

                header = tasks[0]
                dataRows = tasks[1:]

                for row in dataRows:
                    if len(row) < 3:
                        row.append("Not Started")

                for task in dataRows:
                    print(
                        f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.\n")

    elif viewTaskOptions == 2:
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [row for row in reader if row]

                if len(tasks) <= 1:
                    print("No tasks found. Please add a task first.\n")
                    return
                dataRows = tasks[1:]

                for task in dataRows:
                    print(
                        f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |\n")

                editTaskNameOptions = (
                    input("Please enter the id of the task name you'd like to change: "))
                newTaskName = input("Please enter new task name: ").title()

                header = tasks[0]
                dataRows = tasks[1:]

                changedTask = []
                unchangedTask = []
                for task in dataRows:
                    if task[0] in editTaskNameOptions:
                        task[1] = newTaskName
                        changedTask.append(task)
                    else:
                        unchangedTask.append(task)

                with open(FILENAME, "w", newline="") as file:
                    allTasks = [header] + unchangedTask + changedTask
                    writer = csv.writer(file)
                    writer.writerows(allTasks)
                    print(allTasks)
                    print("Task Name Changed Successfully")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.\n")
            return

    elif viewTaskOptions == 3:
        return
    else:
        print("Invalid Option")
        return


def complete_Task():
    """
    Mark tasks as completed.

    Displays all current tasks and allows the user to select tasks by ID
    to mark as "Completed". Updates the CSV file with the new status.
    """
    print("You're On Complete Tasks")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader if row]

            if len(tasks) <= 1:
                print("No tasks found. Please add a task first.\n")
                return

            header = tasks[0]
            data_rows = tasks[1:]

            for task in data_rows:
                print(
                    f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.\n")
        return

    completeTaskOptions = int(input("1.Complete Task\n2.Return to menu\n"))
    if completeTaskOptions == 1:
        completeTasks = input(
            "Please enter the task ID's you'd like to mark as complete seperated by commas e.g. 1,2,3 ")
        completeTasks = [x.strip() for x in completeTasks.split(",")]

        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [row for row in reader if row]

                if len(tasks) <= 1:
                    print("No tasks found. Please add a task first.\n")
                    return

            updated_tasks = []
            for task in tasks:
                if task[0] in completeTasks:
                    task[2] = "Completed"
                updated_tasks.append(task)

            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_tasks)
            print("Tasks marked as completed successfully.")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.\n")
            return

    elif completeTaskOptions == 2:
        return
    else:
        print("Invalid Option")
        return


def delete_Task():
    """
    Delete tasks from the CSV file.

    Displays all tasks and allows the user to remove tasks by specifying
    their IDs. Updates the CSV to only keep remaining tasks.
    """
    print("You're On Delete Tasks")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader if row]

            if len(tasks) <= 1:
                print("No tasks found. Please add a task first.\n")
                return

            header = tasks[0]
            data_rows = tasks[1:]

            for task in data_rows:
                print(
                    f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.\n")
        return

    deleteTaskOptions = int(input("1.Delete Task\n2.Return to menu\n"))
    if deleteTaskOptions == 1:
        deleteOptions = input(
            "Please enter the task ID's you'd like to delete separated by commas e.g. 1,2,3: ")
        deleteOptions = [x.strip() for x in deleteOptions.split(",")]

        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [rows for rows in reader if rows]

                if len(tasks) <= 1:
                    print("No tasks found. Please add a task first.\n")
                    return

            deleted_Tasks = []
            kept_Tasks = []
            for task in tasks:
                if task[0] in deleteOptions:
                    deleted_Tasks.append(task)
                else:
                    kept_Tasks.append(task)

            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(kept_Tasks)
            print("Tasks deleted successfully.")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.\n")
            return


def menu():
    """
    Main application menu loop.

    Allows the user to navigate between:
    - Adding tasks
    - Viewing or editing tasks
    - Completing tasks
    - Deleting tasks
    - Exiting the application
    """
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
