from pooltable import *
from checkinput import numbercheck

def refreshScreen():
    print(chr(27) + "[2J")
    viewAllTables()
    print "\n"

while True:
    print(chr(27) + "[2J")
    choice = raw_input('''
Enter 'q' to quit the program at any time.

You may enter 1 to see the status of all tables,
              2 to give a table out to a customer,
              3 to close a table out when finished,
          and 4 to e-mail out the report from today.

What would you like to do? ''')
    if choice == 'q':
        print(chr(27) + "[2J")
        break
    elif choice == '1':
        refreshScreen()
        raw_input("Press Enter to continue...")
    elif choice == '2':
        refreshScreen()
        i = int(numbercheck("Which pool table number would you like to give out? "))
        if 0 < i < 13:
            pooltable[i-1].giveOut()
        refreshScreen()
        raw_input("Press Enter to continue...")
    elif choice == '3':
        refreshScreen()
        i = int(numbercheck("Which pool table number would you like to close out? "))
        if 0 < i < 13:
            pooltable[i-1].closeOut()
        refreshScreen()
        print("Please let the customer know that they owe ${0:.01} for {1} of game time.".format(pooltable[i-1].cost, pooltable[i-1].readableTime()))
        print("")
        raw_input("Press Enter to continue...")
    elif choice == '4':
        emailReport()
        raw_input("Press Enter to continue...")
    else:
        print "Sorry, that is not a valid input."
    else:
