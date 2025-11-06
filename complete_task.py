def complete_task():
    running_complete = True
    while running_complete == True:
        mynum = int(input('Enter 1 to complete a task, enter 2 to exit.'))
        if mynum == 1:
            line_to_remove = int(input('Enter the number of the task to be marked as complete: '))
            file_path = "tasks.txt"
            completed_file = "completed_tasks.txt"

            removed_line = lines[line_to_remove - 1]  

            with open(file_path, "r") as file:
                lines = file.readlines()

            with open(file_path, "w") as file:
                file.writelines([line for i, line in enumerate(lines, start=1) if i != line_to_remove])

            with open(completed_file, "a") as completed:
                completed.write(removed_line)

            print(f"Task {line_to_remove} marked as completed, and added to Completed Tasks List")

        elif mynum == 2:
            running_complete = False
        else:
            print('Invalid input.')