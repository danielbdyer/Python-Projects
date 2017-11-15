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
