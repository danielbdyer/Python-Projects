class Address():
    def __init__(self,street,state,zipCode):
        self.street = street
        self.state = state
        self.zipCode = zipCode

class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.addresses = []
        # One to many relationship.

customer = Customer()
customer.firstName = "Azam"
customer.lastName = "Sharp"

address1 = Address("1200 Richmond Ave.","TX","77042")
address2 = Address("3200 Harwin Ave.","TX","77098")
address3 = Address("1234 Woodlands","TX","77089")

customer.addresses.append(address1)
customer.addresses.append(address2)
customer.addresses.append(address3)

print(customer.firstName + " " + customer.lastName)
for address in customer.addresses:
    print(address.street + " " + address.state)
    print("\n")

###

class Job(object):
    def __init__(self):
        self.title = ""
        self.location = ""
        self.department = ""

class Employee(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.job = Job()

employee = Employee("Daniel","Dyer")
employee.job.title = "Fullstack Engineer"
employee.job.location = "DigitalCrafts"
employee.job.department = "November cohort"

print(employee.firstName + " " + employee.lastName)
print(employee.job.title + " at " + employee.job.location)
