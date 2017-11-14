first_name = raw_input("What is your first name? ")
last_name = raw_input("What is your last name? ")

#age = raw_input("What is your age? ")
#message = name + age
#message = "My name is " + name + " and my age is " + age + "."

message = "Hello, My name is {0}, {1}".format(first_name,last_name)

print(message)
