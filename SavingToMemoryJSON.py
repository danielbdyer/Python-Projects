import json

class Task(object):
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority

    def toDictionary(self):
        return {"title":self.title,"priority":self.priority}

newTask = Task('Mail the stuff','Hard')

filename = 'tasks.json'

#task1 = {"title":"Wash the car","priority":"high"}
#task2 = {"title":"Feed the cat","priority":"medium"}

#tasks = [task1,task2]

with open(filename,'w') as file_object:
    json.dump(newTask.toDictionary(),file_object, sort_keys=True, indent=4)
    #json.dump(tasks, file_object)

with open(filename) as file_object:
    #arrayOfDictionaries = json.load(file_object)
    dictionary = json.load(file_object)
    t = Task(dictionary["title"],dictionary["priority"])
    print(str(t.title),str(t.priority))
