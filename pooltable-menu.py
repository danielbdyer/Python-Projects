from pooltable import *

while True:
    choice = raw_input('Please input command: ')
    if choice == 'q':
        print "\n"
        break
    else:
        result = eval(str(choice))
