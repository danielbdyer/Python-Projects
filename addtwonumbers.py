from checkint import numbercheck

print(chr(27) + "[2J")

print('''Welcome to this way-too-fancy command line number adder!
We are here to serve you, and wish you well in your number-adding pursuits.''')
number_1 = numbercheck("To begin, please type your first number now: ")
number_2 = numbercheck("Great! And the second? ")

total_number = int(number_1 + number_2)

print("Fantastic! I have calculated that the sum total of these two integers is {0}.".format(total_number))
print("We thank you for using this way-too-fancy command line number adder. Please come again!")

exit()
