# USING GLOBAL for solving some problems

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is "+x)
