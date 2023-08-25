import sys

# Displaying Task
print("Task Added Successfully")

# Loop through the command line arguments and print each task
for items in enumerate(sys.argv[1:]):
    task = ' '.join(map(str, items))
    print(task)

# Displaying menu
print("To-Do-List".center(100))
print("Enter 2 to delete Task\n")


# User input for choice
user_choice = int(input(">>>"))

# Matching the user's choice
if user_choice == 2:
    # Function to delete a task
    def truncate_task():
        tasks = []
        
        # Loop through the command line arguments and split each task
        for task in enumerate(sys.argv[1:]):
            task_str = ' '.join(map(str, task))
            tasks.extend(task_str.split("\n"))
            
        print(tasks)

        # Get the index of the task to be deleted from the user
        index = int(input("Enter index: "))

        # Remove the task at the given index
        del tasks[index]

        print("Task deleted Successfully!")

        # Print the remaining tasks
        for incomplete_task in tasks:
            print(incomplete_task)

    truncate_task()
    
# Comments:
# - The code starts by displaying the tasks that were passed as command line arguments.
# - The menu is displayed with an option to delete a task.
# - The user is prompted to enter their choice.
# - If the user chooses 2, the truncate_task function is called to delete a task.
# - The truncate_task function:
#   - Initializes an empty list to store the tasks.
#   - Loops through the command line arguments and splits each task string by newline.
#   - Gets the index of the task to be deleted from the user.
#   - Removes the task at the given index from the tasks list.
#   - Prints a success message.
#   - Prints the remaining tasks.