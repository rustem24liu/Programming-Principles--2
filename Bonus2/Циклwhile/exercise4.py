n = int(input())
m = int(input())

cnt = 0
i = n
while i < m:
    while n < m:
        n = n*0.1+n
        cnt+=1
    i+=1
print(cnt+1)
"""
cnt2 = 1
while n < m:
    cnt2+=1
    n += n*0.1
print(cnt2)"""