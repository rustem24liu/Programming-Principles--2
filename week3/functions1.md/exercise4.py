numbers = [int(i) for i in input().split()]
def filter_primes(numbers):
    result = []
    for x in numbers:
        if x > 1:
            for i in range(2, x):
                if x % 2 == 0:
                    break
            else:
                result.append(x)
    return result
print(filter_primes(numbers))