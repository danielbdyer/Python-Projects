names = ["Alex", "Bob", "Danny", "John", "Mary", "Steve"]
print("The names you have available to you are: {0}.".format(names))
nameToDelete = str(raw_input("What name should I search for? "))
indexToDelete = -1

for index in range(0,len(names)):
    if nameToDelete.lower() == names[index].lower():
        print "'%s' was found in the list! I'll delete that for you." % names[index]
        indexToDelete = index
        break

if indexToDelete != -1:
    del names[indexToDelete]
    print "Here's the new list, without that name."
    print names
else:
    print("I couldn't find the searched name. Please try again!")
