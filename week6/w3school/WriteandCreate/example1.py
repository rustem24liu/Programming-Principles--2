f = open('demofile2.txt', "a")
f.write("Hello my name is Gustafo!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())