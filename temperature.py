#celsius_input = raw_input("Enter temperature in celsius: ")
#print("You entered {0} degrees celsius.".format(celsius_input))
#convert_temp = (int(celsius_input) * 1.8) + 32
#print(convert_temp)

def celsius_to_fahrenheit(cel_temp):
    fahr_temp = (int(cel_temp) * 1.8) + 32
    print("Your temperature in fahrenheit is {0} degrees.".format(fahr_temp))
    return fahr_temp

cel_temp = int(raw_input("Enter temperature in celsius: "))
celsius_to_fahrenheit(cel_temp)
