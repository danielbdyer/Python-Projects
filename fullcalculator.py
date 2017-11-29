from calculator import Calculator
from checkinput import *

calculator = Calculator()

def calculate():
    first_int = numbercheck("What's your first integer? ")
    operand = operandcheck('''What's your operand you'd like to use?
(You may use '+' or '-' or '*' or '/' or '!'.) ''')

    if operand == '!':
        answer = calculator.fact(first_int)
    else:
        second_int = numbercheck("What's your second integer? ")

        if operand == '+':
            answer = calculator.add(first_int,second_int)
        elif operand == '-':
            answer = calculator.sub(first_int,second_int)
        elif operand == '*':
            answer = calculator.mult(first_int,second_int)
        elif operand == '/':
            answer = calculator.div(first_int,second_int)
        else:
            print('''You did not enter a valid operand in step 2, sorry!
    Exiting program, please try again.''')
            return

    print("Congratulations! Your answer is {0}.".format(answer))

print(chr(27) + "[2J")
calculate()
