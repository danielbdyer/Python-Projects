tasks = []

class Task(object):
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority.title()

    def __eq__(self,other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.title == other.title

def addTask(title,priority):
    task = Task(title,priority)
    if task not in tasks:
        tasks.append(task)

def removeTask(index):
    human_readable_index = int(index) - 1
    del tasks[human_readable_index]
    print "\n Task deleted. Your tasks are now:"
    viewTasks()

def viewTasks():
    print ""
    for index, elem in enumerate(tasks):
        print(str(index+1) + ". " + elem.title + " [" + elem.priority + "]")
    if len(tasks) == 0:
        print("\nThere are no tasks currently in your list, so please add some!")



while True:
    choice = raw_input('''
    Press 1 to add a new task.
    Press 2 to delete a task.
    Press 3 to review all tasks.
    Press q to quit the app.\n
    Enter your command here: ''')

    if choice == "1":
        title = raw_input("\nEnter the title of your task. ")
        priority = raw_input("Please input the priority of this task. ")

        addTask(title,priority)
        print("\nAdded item to your to-do list:")
        viewTasks()

    if choice == "2":
        viewTasks()
        if len(tasks) != 0:
            title = raw_input("\nWhich task are you finished with? ")
            removeTask(title)

    if choice == "3":
        viewTasks()

    if choice == "q":
        print "\n"
        break
