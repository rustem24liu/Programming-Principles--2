def prime_find(n):
    for i in range(2,n,1):
        if n%i==0:
         return False
    return True
n=input().split()

prime_nums=list(filter(lambda x:prime_find(int(x)), n))
print(prime_nums)