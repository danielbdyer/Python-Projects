class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = "" # could also go into arguments above.
        self.age = -1
        self.height = 0
        self.weight = 0

#    def walk(self):
    #    print "{1} is walking." % format(str(self.firstName))

#    def talk(self):
    #    print "{1} is talking." % format(str(self.firstName))

#    def sing(self,songName):
    #    print "{1} is singing {2}." % format(str(self.firstName), str(self.songName))


person1 = Person('Danny', 'Dyer')
print(person1.firstName)
print(person1.lastName)
person1.age = 27
person1.weight = 200
#person1.walk()


class Car(object):
    # Sets a reference to the default parent object.
    def __init__(self,make,model):
            # A special method/function inside the class
            # responsible for initializing the class.
        self.make = make
        self.model = model

        # noOfCylinders = 4 // won't work!
        self.noOfCylinders = 4

        # self defines the instance of the object of the class.

    def start(self):
        print "Starting the car through spark ignition."

    # Passing 'self' as an argument is not common in other languages.
    # But Python is explicit and wants you to refer to your object.

class ElectricCar(Car):
    def __init(self):
        super(ElectricCar,self.__init__('Tesla','Model X'))

    def start(self):
        print("Starting the electric vehicle.")


electric_car = ElectricCar()
print(electric_car.make)
print(electric_car.model)
electric_car.start()

bmw = Car('BMW', 'Series 3')
print(bmw.make)
print(bmw.model)
# print(bmw.noOfCylinders) // does not work!
bmw.start()

toyota = Car('Toyota', 'Camry')
print(toyota.make)
print(toyota.model)
