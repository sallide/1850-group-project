def add_task():
    running_add = True
    while running_add == True:
        file = open('tasks.txt', 'a')
        mynum = int(input('Enter 1 to add task, enter 2 to exit.'))
        if mynum == 1:
            name = input('Enter the name of your task: ')
            description = input('Enter a description for your task: ')
            date = input('Enter a due date for your task: ')
            completed = False
            f = open('tasks.txt', 'r')
            count = len(f.readlines())+1
            myline = (f'\n{count}. Name: {name}, Description: {description}, Due date: {date}, Completed: {completed}.')
            file.write(myline)
        elif mynum == 2:
            running_add = False
        else:
            print('Invalid input.')
    

