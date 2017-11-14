print(chr(27) + "[2J")

def numbercheck(prompt):
    while True:
        try:
            val = int(input(prompt))
        except ValueError:
            print("That's not an int!")
            continue
        except NameError:
            print("That's not even a number!")
        else:
            break
    return val

print('''Welcome to this way-too-fancy command line number adder!
We are here to serve you, and wish you well in your number-adding pursuits.''')
number_1 = numbercheck("To begin, please type your first number now: ")
number_2 = numbercheck("Great! And the second? ")

total_number = number_1 + number_2

print("Fantastic! I have calculated that the sum total of these two integers is {0}.".format(total_number))
print("We thank you for using this way-too-fancy command line number adder. Please come again!")

exit()
