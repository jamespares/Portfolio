# importing libraries
from datetime import datetime

# defining functions
def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# program starts
with open('user.txt', 'r') as user_file:
    usernames = [] # creating list to store usernames and passwords
    passwords = []

    for line in user_file:
        if line.strip():  # This checks if the line is not empty
            text = line.strip().split(',')  # strips white space and removes delimiter
            if len(text) == 2:  # Ensures only two units in the index (username and password)
                usernames.append(text[0].strip())
                passwords.append(text[1].strip())
            else:
                print(f"Warning: Malformed line detected - {line}")

username = input('What is your username: ').strip()
password = input('What is your password: ').strip()

is_authenticated = False # tag to ensure full code only runs when logged in

if username in usernames:
    index = usernames.index(username)
    if password == passwords[index]:
        print("You're in")
        is_authenticated = True
    else:
        print('Incorrect password. Please try again')
else:
    print('Incorrect details. Please try again')

if is_authenticated:
    if username.strip() == 'admin': # ensures full options only accessible to admin
        while True:
            menu = input(
                '''Select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                s - view statistics
                e - exit
                : '''
            ).lower()

            if menu == 'r':
                new_username = input('What is your desired username? ')
                while True:
                    new_password = input('What is your desired password? ')
                    new_password2 = input('Please repeat password: ')
                    if new_password2 == new_password:
                        with open('user.txt', 'a') as user_file:
                            user_file.write(f'\n{new_username},{new_password}')
                            usernames.append(new_username) # add new usernames to list
                            passwords.append(new_password) # add new passwords to list
                        print('Registration complete')
                        break
                    else:
                        print('Passwords do not match!')

            elif menu == 's':
                with open('user.txt', 'r') as user_file:
                    no_users = 0
                    for each_line in user_file:
                        if each_line.strip():
                            no_users += 1

                with open('tasks.txt', 'r') as task_file:
                    no_tasks = 0
                    for each_line in task_file:
                        if each_line.strip():
                            no_tasks += 1

                print(f'''
    Number of users: {no_users}
    Number of tasks: {no_tasks}
                ''')

            if menu == 'a':
                with open('tasks.txt', 'a') as task_file:
                    username_owner = input('Who is the task assigned to? ')
                    task = input('What is the title of the task? ')
                    task_description = input('What is the description of the task? ')

                    # validate due date format
                    while True:
                        due_date = input('What is the due date of the task? ')
                        if validate_date_format(due_date):
                            break
                        else:
                            print("Invalid date format. Please use YYYY-MM-DD")

                    # validate current date format
                    while True:
                        current_date = input('What is the current date? ')
                        if validate_date_format(current_date):
                            break
                        else:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            # this format allows sorting by broadest category first

                    task_complete = input('Is task complete? ')
                    task_file.write(
                        f'\n{username_owner},{task},{task_description},{due_date},{current_date},{task_complete}')
                    print('Task added')

            elif menu == 'va':
                with open('tasks.txt', 'r') as task_file:
                    for each_line in task_file:
                        task = each_line.strip().split(',')
                        if len(task) == 6: # using indexing to define variables based on input order
                            task_owner = task[0]
                            task_name = task[1]
                            task_description = task[2]
                            due_date = task[3]
                            current_date = task[4]
                            task_status = task[5]
                            print(f'''
    Task:            {task_name}
    Assigned to:     {task_owner}
    Date Assigned:   {current_date}
    Due Date:        {due_date}
    Task Complete?   {task_status}
    Task Description:{task_description}
                            ''')

            elif menu == 'vm':
                with open('tasks.txt', 'r') as task_file:
                    has_tasks = False
                    for each_line in task_file:
                        task = each_line.strip().split(',')
                        if len(task) == 6:
                            task_owner = task[0]
                            task_name = task[1]
                            task_description = task[2]
                            due_date = task[3]
                            current_date = task[4]
                            task_status = task[5]

                        if task_owner == username: # print only the tasks assigned to username
                            has_tasks = True
                            print(f'''
    Task:            {task_name}
    Assigned to:     {task_owner}
    Date Assigned:   {current_date}
    Due Date:        {due_date}
    Task Complete?   {task_status}
    Task Description:{task_description}
                            ''')

                if not has_tasks:
                    print('You have no tasks assigned') # if no tasks make it clear

            elif menu == 'e':
                print('Goodbye!!!')
                exit()

    while True: # while and if loops running the non-admin menu
        menu = input(
            '''Select one of the following options:
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit
            : '''
        ).lower()

        if menu == 'a':
            with open('tasks.txt', 'a') as task_file:
                username_owner = input('Who is the task assigned to? ')
                task = input('What is the title of the task? ')
                task_description = input('What is the description of the task? ')

                # validate due date format
                while True:
                    due_date = input('What is the due date of the task? ')
                    if validate_date_format(due_date):
                        break
                    else:
                        print("Invalid date format. Please use YYYY-MM-DD")

                # validate current date format
                while True:
                    current_date = input('What is the current date? ')
                    if validate_date_format(current_date):
                        break
                    else:
                        print("Invalid date format. Please use YYYY-MM-DD.")

                task_complete = input('Is task complete? ')
                task_file.write(f'\n{username_owner},{task},{task_description},{due_date},{current_date},{task_complete}')
                print('Task added')

        elif menu == 'va':
            with open('tasks.txt', 'r') as task_file:
                for each_line in task_file:
                    task = each_line.strip().split(',')
                    if len(task) == 6:
                        task_owner = task[0]
                        task_name = task[1]
                        task_description = task[2]
                        due_date = task[3]
                        current_date = task[4]
                        task_status = task[5]
                        print(f'''
Task:            {task_name}
Assigned to:     {task_owner}
Date Assigned:   {current_date}
Due Date:        {due_date}
Task Complete?   {task_status}
Task Description:{task_description}
                        ''')

        elif menu == 'vm':
            with open('tasks.txt', 'r') as task_file:
                has_tasks = False
                for each_line in task_file:
                    task = each_line.strip().split(',')
                    if len(task) == 6:
                        task_owner = task[0]
                        task_name = task[1]
                        task_description = task[2]
                        due_date = task[3]
                        current_date = task[4]
                        task_status = task[5]

                    if task_owner == username:
                        has_tasks = True
                        print(f'''
Task:            {task_name}
Assigned to:     {task_owner}
Date Assigned:   {current_date}
Due Date:        {due_date}
Task Complete?   {task_status}
Task Description:{task_description}
                        ''')

            if not has_tasks:
                print('You have no tasks assigned')

        elif menu == 'e':
            print('Goodbye!')
            exit() # code stops