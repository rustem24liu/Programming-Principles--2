numbers = [int(i) for i in input().split()]

def filter(numbers):
    result = []
    for x in numbers:
        if x > 1:
            for i in range(2, x):
                if x%i == 0:
                    break
            else:
                result.append(x)
    print(result)
filter(numbers)