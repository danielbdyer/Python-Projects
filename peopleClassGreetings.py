class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people_greeted = []

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        if other_person not in self.unique_people_greeted:
            self.unique_people_greeted.append(other_person)

    def print_contact_info(self):
        print "%s's email: %s; %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)
        other_person.friends.append(self)

    def num_friends(self):
        print("%s's number of friends is: %s" % (self.name, len(self.friends)))

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print "This many unique people greeted: %s" % str(len(self.unique_people_greeted))



sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
dee_ann = Person('Dee Ann','dee.ann@yahoo.com','342-423-1423')

sonny.greet(jordan)
print("Sonny's greeting count: " + str(sonny.greeting_count))

jordan.greet(sonny)

print(sonny.email)
print(sonny.phone)

sonny.print_contact_info()

jordan.add_friend(sonny)
jordan.num_friends()
sonny.num_friends()

sonny.greet(jordan)
print("Sonny's greeting count: " + str(sonny.greeting_count))
sonny.num_unique_people_greeted()

sonny.greet(dee_ann)
print("Sonny's greeting count: " + str(sonny.greeting_count))
sonny.num_unique_people_greeted()


class Vehicle(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year + " " + self.make + " " + self.model)

car = Vehicle('Nissan','Leaf', '2015')
print car.make, car.model, car.year
car.print_info()
