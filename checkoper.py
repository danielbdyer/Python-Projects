def operandcheck(prompt):
    operand = raw_input(prompt)
    while operand not in ('+', '-', '*', '/', '!'):
        print("That's not a valid operand!")
        print("Please try again using '+', '-', '*', '/', '!'.")
        operand = raw_input("What's your operand you'd like to use? ")
    return operand
