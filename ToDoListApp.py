import csv

FILENAME = "TaskList.csv"


def add_Task():
    print("Add Tasks\n")
    addTaskOptions = int(input("1.Add New Task\n2.Return to menu\n"))
    if addTaskOptions == 1:
        task = input("Enter a new task: ").title()
        status = "Not Started"  # Default status for new tasks
        dueDate = input("Please enter the due date: ")
        priority = input(
            "Please enter the priority(Low/Medium/High): ").title()
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
                        writer.writerow(
                            ["ID", "Task", "Status", "Due Date", "Priority"])
                else:
                    # If header exists, subtract 1 to get actual number of tasks
                    new_id = len(rows) if rows[0][0] != "ID" else len(rows)
        except FileNotFoundError:
            # If file doesn't exist, create it and write header and sets the first id to 1
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ID", "Task", "Status", "Due Date", "Priority"])
            new_id = 1

        # Append the new task with ID and status
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
    print("View Tasks\n")
    viewTaskOptions = int(
        input("1.View All Tasks\n2.Edit Task Name\n3.Return to menu\n"))

    if viewTaskOptions == 1:
        # view all tasks code below
        try:
            with open(FILENAME, "r", newline="") as file:
                reader = csv.reader(file)
                tasks = [row for row in reader if row]  # Skip empty rows

                if len(tasks) <= 1:  # Only header or empty
                    print("No tasks found. Please add a task first.\n")
                    return

                header = tasks[0]
                dataRows = tasks[1:]  # Exclude header

                # Upgrade old tasks that have only ID and Task
                for row in dataRows:
                    if len(row) < 3:  # Status missing
                        row.append("Not Started")

                # Print tasks
                for task in dataRows:
                    print(
                        f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |")

        except FileNotFoundError:
            print("No tasks found. Please add a task first.\n")

    # edit task name code below
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

                # code below changes the name of the task
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


def complete_Task():  # This function displays all the tasks and asks the user to input 1 if they want to input the ID of the task they want to mark as complete or 2 to return to the menu
    print("You're On Complete Tasks")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader if row]  # Skip empty rows

            if len(tasks) <= 1:  # Only header or empty
                print("No tasks found. Please add a task first.\n")
                return

            header = tasks[0]
            data_rows = tasks[1:]  # Exclude header

            # Print tasks
            for task in data_rows:
                # Run through all tasks inside data_rows and display all tasks as ID, Task and Status
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
                # turns it into a list filtering out any blank lines
                tasks = [row for row in reader if row]

                if len(tasks) <= 1:  # Only header or empty (less than 1 default item which is the header)
                    print("No tasks found. Please add a task first.\n")
                    return

            # Update the status of the specified tasks
            updated_tasks = []  # new empty list to hold all tasks after modification
            for task in tasks:
                # if the task ID is in the list of IDs to complete
                if task[0] in completeTasks:
                    task[2] = "Completed"  # Update status to Completed
                updated_tasks.append(task)

            # Write the updated tasks back to the file
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
    print("You're On Delete Tasks")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader if row]  # Skip empty rows

            if len(tasks) <= 1:  # Only header or empty
                print("No tasks found. Please add a task first.\n")
                return

            header = tasks[0]
            data_rows = tasks[1:]  # Exclude header

            # Print tasks
            for task in data_rows:
                # Run through all tasks inside data_rows and display all tasks as ID, Task, and Status
                print(
                    f"| ID: {task[0]} | Task: {task[1]} | Status: {task[2]} | Due Date {task[3]} | Priority {task[4]} |")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.\n")
        return

    deleteTaskOptions = int(input("1.Delete Task\n2.Return to menu\n"))
    if deleteTaskOptions == 1:
        deleteOptions = input(
            "Please enter the task ID's you'd like to delete separated by commas e.g. 1,2,3: ")
        # turns "1,2,3" → ["1", "2", "3"]
        # Used list comprehension here. x is each item from the result of split(",") and x.strip removes any extra spaces before and after the text
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
