num = int(raw_input("What number would you like to factorialize? "))

def factorializeThis(num):
    if num <= 1:
        return num
    else:
        return num * factorializeThis(num - 1)

print(factorializeThis(num))