filename = "helloworld.txt"

with open('filename.txt') as file_object: # if you don't specify w or a as
    contents = file_object.read()         # a parameter you're essentially
    print(contents)                       # saying just read the file i.e. here

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip('\n'))

with open('filetowrite.txt','w') as file_object: # writes/overwrites
    file_object.write("Bye world.")

with open('appendingtofile.txt', 'a') as file_object:
    file_object.write("Bye world.")
    file_object.write("\n")
