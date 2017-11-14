def numbercheck(prompt):
    while True:
        try:
            val = float(input(prompt))
        except ValueError:
            print("That's not an int!")
            continue
        except NameError:
            print("That's not even a number!")
        else:
            break
    return val
