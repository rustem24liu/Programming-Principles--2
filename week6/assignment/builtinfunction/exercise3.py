def my3():
    string = input()
    if string[::-1] == string:
        print("Yes, that is palindrom string")
    else:
        print("NO, that is NOT polindrom string")

my3()