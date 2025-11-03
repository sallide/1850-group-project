running = True
while running == True:
    choice = int(input(f' 1. Add a new task.\n 2. Mark a task as complete.\n 3. Remove a task.\n 4. Edit a task.\n 5. Display all tasks.\n 6. Exit.'))
    if choice == 1:
        from add_task import *
        add_task()
    elif choice == 2:
        #function not created yet
        from complete_task import *
        complete_task()
    elif choice == 3:
        #function not created yet
        from remove_task import *
        remove_task()
    elif choice == 4:
        #function not created yet
        from edit_task import *
        edit_task
    elif choice == 5:
        #function not created yet
        from display_task import *
        display_task
    elif choice == 6:
        running = False
    else:
        print('Invalid input.')