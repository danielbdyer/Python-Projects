import json
filename = 'tasks.json'
import itertools

tasks = []

class Task(object):
    newid = itertools.count(1).next
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.id = Task.newid()

    def toDictionary(self):
        return {"title": self.title, "priority": self.priority, "id": self.id}

def load_all_tasks():
    with open('tasks.json') as file_object:
        tasks = json.load(file_object)


def addTask(title,priority,id):
    newTask = Task(title,priority)
    print newTask.id
    if newTask.id == 1:
        with open(filename,'w') as file_object:
            json.dump(newTask.toDictionary(),file_object, sort_keys=True, indent=4)
    else:
        print "Trying to append"
        with open(filename,'a+') as file_object:
            tasks = json.load(tasks.json)
            print tasks
            tasks.append(newTask.toDictionary())
            print tasks
            json.dump(tasks, file_object, sort_keys=True, indent=4)

def viewTasks():
    with open(filename, 'r') as file_object:
        arrayOfDictionaries = json.load(file_object)
        print(arrayOfDictionaries)

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

        addTask(title,priority,id)
        print("\nAdded item to your to-do list:")
        #viewTasks()

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
