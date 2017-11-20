class Animal(object):
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def run(self):
        print("Running like a normal animal.")

    def walk(self):
        print("I am walking.")

    def eat(self):
        print("I am eating.")

class Cheetah(Animal):

    # A class can only have one parent.

    def __init__(self):
        super(Cheetah,self).__init__('Cheetah','Cats') # initializes
        self.name = ""

    def run(self):
        print("Cheetah is running super fast.")


# Creating an object of animal class.
cat = Animal('Lynx','cat species')
cat.walk()
cat.eat()

ch = Cheetah()
ch.run()
print(ch.species)
