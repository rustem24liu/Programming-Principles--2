f = open("myfile.txt", "x") #* 'x' is create the new file
(f.write("But you can call me GUS"))

f = open("myfile.txt", "r")
print(f.read())