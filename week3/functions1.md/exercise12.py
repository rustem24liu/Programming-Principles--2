sizes = [int(i) for i in input().split()]

def histogram(sizes):
    for x in sizes:
        for i in range(x):
            print('*', end = '')
        print()

histogram(sizes)