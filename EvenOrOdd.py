from checkint import numbercheck
print(chr(27) + "[2J")

print("Would you like to check to see if a number is even or odd? Enter it below!")
unknown_int = int(numbercheck("What's your number? "))

if (unknown_int%2==0): print("{0} is even!".format(unknown_int))
else: print("{0} is odd!".format(unknown_int))
