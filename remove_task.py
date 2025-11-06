def remove_task():
    running_remove = True
    while running_remove == True:
        mynum = int(input('Enter 1 to remove a task, enter 2 to exit.'))
        if mynum == 1:
            line_to_remove = int(input('Enter the number of the task to be removed: '))
            file_path = "tasks.txt"

            with open(file_path, "r") as file:
                lines = file.readlines()

            with open(file_path, "w") as file:
                file.writelines([line for i, line in enumerate(lines, start=1) if i != line_to_remove])

        elif mynum == 2:
            running_remove = False
        else:
            print('Invalid input.')