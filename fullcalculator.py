import calculatefunction
from checkint import numbercheck
from checkoper import operandcheck

def calculate():
    first_int = numbercheck("What's your first integer? ")
    operand = operandcheck('''What's your operand you'd like to use?
(You may use '+' or '-' or '*' or '/'.) ''')
    second_int = numbercheck("What's your second integer? ")

    if operand == '+':
        answer = calculatefunction.add(first_int,second_int)
    elif operand == '-':
        answer = calculatefunction.sub(first_int,second_int)
    elif operand == '*':
        answer = calculatefunction.mult(first_int,second_int)
    elif operand == '/':
        answer = calculatefunction.div(first_int,second_int)
        remainder = calculatefunction.remainder(first_int,second_int)
    else:
        print('''You did not enter a valid operand in step 2, sorry!
Exiting program, please try again.''')
        return

    if operand == '/':
        print("Congratulations! Your answer is {0}, with a remainder of {1}".format(answer,remainder))
    else:
        print("Congratulations! Your answer is {0}.".format(answer))

print(chr(27) + "[2J")
calculate()
