s = input()
def polindrom(s):
    res = s[::-1]
    if s == res:
        print(s, "is polindrom word!")
    else:
        print(s, "is NOT polindrom word!!!")
polindrom(s)