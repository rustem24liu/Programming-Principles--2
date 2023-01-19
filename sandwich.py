A = int(input())
B = int(input())
H = int(input())
if H >= A and H <= B :
    print("Это нормально")
elif H < A:
    print("Недосып")
elif H > B:
    print("Пересып")