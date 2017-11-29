def operandcheck(prompt):
    operand = raw_input(prompt)
    while operand not in ('+', '-', '*', '/', '!'):
        print("That's not a valid operand!")
        print("Please try again using '+', '-', '*', '/', '!'.")
        operand = raw_input("What's your operand you'd like to use? ")
    return operand

def numbercheck(prompt):
    while True:
        try:
            val = float(input(prompt))
        except ValueError:
            print("That's not an int!")
            continue
        except NameError:
            print("That's not even a number!")
            continue
        except TypeError:
            print("Pssh! What kind of number is that?")
            continue
        else:
            break
    return val
