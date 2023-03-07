f = open("demofile2.txt", "w")
f.write("Woops! I've deleted the content!")

f = open("demofile2.txt", "r")
print(f.read())