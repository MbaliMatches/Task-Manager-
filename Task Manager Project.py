# =================================== PROJECT: TASK MANAGER =================================== #
'''This is a program that assists a small business manage tasks assigned to each team member'''

# import libraries
'''this module will be used later in the program to specify an exact time that a task has been accessed'''
''' this module will bw used later in the program to find pathways for text files stored on the operating system '''
from datetime import datetime
import os
from tabulate import tabulate

# ==========FUNCTION DEFINIIIONS========== #
'''The functions that will be used for the functionality of the program will be defined here '''

# ==========REGISTERING A USER========== #
# when the user chooses the option r, they choose to register a new user 
# the admin is the only one that has been athorized to perform this action 
# the admin adds the new username and paswords, confirms the password 
# if the passwords match the the new username and password are added to the user.txt file that contains all credentails 
# and the program states that the new user has been addded successfully else the admin is given the relevant error code and prompted to confirm the new password   
# the program then makes the user exist the function if they are not the user 
# the while loop is initialized so that the user is prompted to enter a username that is not on the user.txt file until the condition is met

def reg_user():
    try:
        if username != "admin" and password != "adm1n":
            print("Only admin can register new users.")
            return   
    except NameError as e:
        print(f"Error: {e}")  
              
    new_user = input ("Enter a new username: ")
    while new_user in open("user.txt").read():
        print("This username already exists.")
        new_user = input ("Enter a new username: ")
    new_password = input ("Enter a new password: ")
    password_confirm = input ("Please confirm your new password : ")
    if new_password == password_confirm:
        with open ("user.txt", "a") as file:
            file.write("\n") # check if this is the one creating lines between credentials in the user text
            file.write(str(new_user) + "," + " " + (new_password))
            print(f"User {new_user} has been registered successfully !")
    else:
        print("The passwords do not match.")
        password_confirm = input ("Please confirm your new password : ")
        if new_password == password_confirm:
            print(f"User {new_user} has been registered successfully !")                
                
# ==========ADDING A TASK========== #
# when the user chooses the option 'a', they choose to add (append ) a task to the tasks.txt file    
# the user is prompted to input all of the needed information to append to the tasks.txt file       
    
def add_task():       
        with open("tasks.txt", "a") as f :
                print("You are now adding a task")
                asigned_user = input("Who is the owner for this task?\n")     
                title = input("What is the task title?\n")
                description = input("Please enter a description of the task:\n")            
                today = datetime.now().date()
                date_due = input("Please enter when the task is due in dd mmm yyyy format:\n")
                complete = "No"
                f.write(f"{asigned_user}, {title}, {description}, {today}, {date_due}, {complete}\n")
                print ("Task has been successfully added to the task file !")  

# ==========VIEW ALL TASKS========== #
# when the user chooses the option 'va'   
# the program reads the task.txt file , splits the file after each ', ' and tabulates the data in a user-friendly way that will allow the user to 
# see all tasks and relevant information inside of the task 
    
def view_all():                  
        with open ("tasks.txt", "r") as f:
            print ("You are now viewing all tasks")
            tasks = f.readlines()
            for task in tasks :
                task_data = task.split(", ")
                print("-"*50)
                print(f"Task:\t\t\t{task_data[1]}")
                print(f"Assigned to:\t\t{task_data[0]}")
                print(f"Date assigned:\t\t{task_data[3]}")
                print(f"Due date:\t\t{task_data[4]}")
                print(f"Task complete?\t\t{task_data[5]}")
                print(f"Task description:\n{task_data[2]}")
                print("-"*50)  
          
# ==========VIEW MY TASK========== #
# when the user chooses the option 'vm'
# the program reads the tasks.txt file, strips all the whitespaces to ensure that the string is clean and consistent, the string is then stripped ", " 
# the first element is selected from the list obtained after the split operation 
# if the username is the first index in the tasks.txt then the program prints out the task assigned to the user in a user-friendly way 
# user is prompted to select the task that they would like to open this is stored in the variable selected_task// if the user enters -1, the program returns to the main menu 
# converts the selected_task input into an integer within a try-except block to handle invalid numeric inputs.
# checks if the entered task number is within a valid range (1 to task_count)
# initializes task_index to track the task being interacted with.
# loops through the tasks again, similar to the previous loop, but this time focusing on the selected task.
# checks if the selected task is marked as incomplete ("no"),if yes, prompts the user to choose an action (mark as complete or edit).
# depending on the action chosen, it updates the task details and writes the changes back to the "tasks.txt" file.
# if the entered task number is not valid (outside the valid range), it prints an error message.
# if the input cannot be converted to an integer, it catches the ValueError and prints an error message.
 
def view_mine():
    print("You are now viewing your tasks")
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    current_user = tasks[0].strip().split(", ")[0]
    task_count = 0  # Counter to track task numbers

    for idx, task in enumerate(tasks[1:], start=1):
        task_data = task.strip().split(", ")
        if task_data[0] == current_user:
            task_count += 1
            print("-" * 50)
            print(f"Task Number: {task_count}")
            print(f"Task reference:\t\t{task_data[0]}")
            print(f"Task:\t\t\t{task_data[1]}")
            print(f"Assigned to:\t\t{task_data[0]}")
            print(f"Date assigned:\t\t{task_data[3]}")
            print(f"Due date:\t\t{task_data[4]}")
            print(f"Task complete?\t\t{task_data[5]}")
            print(f"Task description:\n{task_data[2]}")
            print("-" * 50)

    selected_task = input("Enter the task number you want to open (-1 to return to the main menu): ")

    if selected_task == "-1":
        return  # Return to the main menu

    try:
        selected_task = int(selected_task)
        if 1 <= selected_task <= task_count:
            task_index = 0  # Index of the selected task in tasks list
            for idx, task in enumerate(tasks[1:], start=1):
                task_data = task.strip().split(", ")
                if task_data[0] == current_user:
                    task_index += 1
                    if task_index == selected_task:
                        if task_data[5].lower() == "no":
                            action = input("Choose an action: Mark as complete (C) or Edit (E): ").lower()
                            if action == "c":
                                task_data[5] = "Yes"  # Mark task as complete
                                tasks[idx] = ", ".join(task_data) + "\n"
                                with open("tasks.txt", "w") as f:
                                    f.writelines(tasks)
                                print("Task marked as complete.")
                            elif action == "e":
                                if task_data[5].lower() == "no":
                                    new_assigned_to = input("Enter the new assigned username: ")
                                    new_due_date = input("Enter the new due date: ")
                                    task_data[0] = new_assigned_to
                                    task_data[4] = new_due_date
                                    tasks[idx] = ", ".join(task_data) + "\n"
                                    with open("tasks.txt", "w") as f:
                                        f.writelines(tasks)
                                    print("Task edited.")
                        else:
                            print("This task has already been completed and cannot be edited.")
                        break
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
       
# ==========READING FILES========== #        
def read_tasks_from_file(filename):
    tasks = []
    with open(filename, "r") as f:
        for line in f:
            task_data = line.strip().split(", ")
            tasks.append(task_data)
    return tasks       

# ==========GENERATING REPORTS========== #
def generate_reports(tasks, total_tasks):
    if menu == 'gr':
        today = datetime.now()
        print("Calculating statistics...")

        completed_tasks = 0
        total_tasks = len(tasks) - 1  

        for task_data in tasks[1:]:
            status = task_data[5]
            if status == "yes":
                completed_tasks += 1

        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task_data in tasks[1:] if task_data[5] == "no" and datetime.strptime(task_data[4], "%d %b %Y" ) < (today))

        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100

        task_overview = [
            ["Total Tasks", total_tasks],
            ["Completed Tasks", completed_tasks],
            ["Uncompleted Tasks", uncompleted_tasks],
            ["Overdue Tasks", overdue_tasks],
            ["Incomplete Percentage", f"{incomplete_percentage:.2f}%"],
            ["Overdue Percentage", f"{overdue_percentage:.2f}%"]
        ]

        user_stats = {}

        for task_data in tasks[1:]:
            user = task_data[0]
            status = task_data[5]
            due_date = datetime.strptime(task_data[4], "%d %b %Y") #converting the due_date from a str to a date.time object

            

            if user not in user_stats:
                user_stats[user] = {
                    'total_assigned': 0,
                    'completed': 0,
                    'uncompleted': 0,
                    'overdue': 0
                }

            user_stats[user]['total_assigned'] += 1
            if status.lower() == 'yes':
                user_stats[user]['completed'] += 1
            else:
                user_stats[user]['uncompleted'] += 1
                if due_date < (today):
                    user_stats[user]['overdue'] += 1

        user_overview = []

        for user, stats in user_stats.items():
            user_overview.append([
                "User",
                user,
                "Total Tasks Assigned",
                stats['total_assigned'],
                "Percentage of Total Tasks Assigned",
                f"{(stats['total_assigned'] / total_tasks) * 100:.2f}%",
                "Percentage of Completed Tasks",
                f"{(stats['completed'] / stats['total_assigned']) * 100:.2f}%",
                "Percentage of Uncompleted Tasks",
                f"{(stats['uncompleted'] / stats['total_assigned']) * 100:.2f}%",
                "Percentage of Overdue Tasks",
                f"{(stats['overdue'] / stats['total_assigned']) * 100:.2f}%"
            ])

        with open("task_overview.txt", "w") as task_file:
            task_file.write("Task Overview\n")
            task_file.write(tabulate(task_overview, headers=["Task Status", "Result"], tablefmt="grid"))

        with open("user_overview.txt", "w") as user_file:
            user_file.write("User Overview\n")
            user_file.write(tabulate(user_overview, headers=["Task Status", "User", "Task Status", "Result", "Task Status", "Result", "Task Status", "Result", "Task Status", "Result"], tablefmt="grid"))
            
        print("Task overview report generated.")


 # ==========DISPLAYING STATISTICS========== #
 # when the user chooses the option 'ds'
 # if the user is not admin they are not granted access to view the statistics 
 # initialize the variable total_users to count  and store the amount of users
 # the user.txt file is open in read mode 
 # total_users then counts the number of lines in the file
 # initialize the variable total_tasks to count and store the amount of tasks
 # the tasks.txt is opened in read mode 
 # for each task in the file, strips the whitespace and then splits the task line into a list of strings using the comma and space as separators
 # for each iteration of the loop, this line increments the total_tasks counter by 1, effectively counting each task.
    
def display_statistics(tasks):
    if menu == 'ds':
        if username != "admin" or password != "adm1n":
            print("Only admin can view statistics.")
            return
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            generate_reports(tasks)
        with open("task_overview.txt", "r") as task_file:
            task_report = task_file.read()

        with open("user_overview.txt", "r") as user_file:
            user_report = user_file.read()

        print("Task Overview Report:")
        print(task_report)
        print("\nUser Overview Report:")
        print(user_report)
tasks = read_tasks_from_file("tasks.txt")   
    
# =========EXIT MENU========== #
# when the user selects 'e' 
# the problems permits the user to exit the programs         
def exit():
    if menu == 'e':
        print('Goodbye') 
        
# this is print statement is ouputted when the user enters an invalid option that is not displayed on the main menu of the program 
def invalid_answer():
    print("You have made a wrong choice.\nPlease Try again")     

# ==========LOGIN SECTION========== #
''''Here the user is prompted to login 
The code opens the user.txt file and reads usernames and passwords from this file 
The user is prompted to enter their username and password 
the contents of the file are stored in the variable credentials 
A boolean condition is initialized, since it is initialized as false the condition in the valid_credentials will always be true 
A loop is that iterates through each line (user_credentials) in the credentials list, the white spaces in the credentials list are stripped 
The username and password are split using the ", ". [0] and [1] assign username and password respectively as they have been split 
If the username inputed is the same as username in list and same for the password the user is logged into the system else they are given a relevant error message
'''

print("Please Login")
with open("user.txt", "r") as file:
    credentials = file.readlines()
valid_credentials = False
while not valid_credentials:
    username = input("Username: ")
    password = input("Password: ")
    for user_credentials in credentials:
        credentials_list = user_credentials.strip().split(", ")
        user_name = credentials_list[0]
        pass_word = credentials_list[1]
        if username == user_name and password == pass_word:
            valid_credentials = True
            break
    if not valid_credentials:
        print("Invalid Credentials\nPlease Try Again.")
if valid_credentials:
    print("Welcome!")
       
# ==========DISPLAY MENU========== #
'''#Here the menu is displayed to the user 
the while True created an infinte loop that enables the program to return to the main menu after running the option that the user has chosen 
the user input is  converted to lowercase using the .lower() string method 
'''
while True:
    menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
Selection: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        tasks = read_tasks_from_file("tasks.txt")
        total_tasks = len(tasks) - 1
        generate_reports(tasks, total_tasks)
    elif menu == 'ds':
        tasks = read_tasks_from_file("tasks.txt")
        display_statistics(tasks)
    elif menu == 'e':
        print('Goodbye')
        break
    else:
        print("Invalid choice. Please try again.")          