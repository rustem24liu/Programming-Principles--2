'''#include <iostream>
using namespace std;
int Fibogo(int n){
    if(n==0) return 0;
    if(n==1) return 0;
    if(n==2) return 1;
    return Fibogo(n-1) + Fibogo(n-2);
}
int main(){
    int n;
    cin >> n;
    cout << Fibogo(n);
}'''
n = int(input())

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(n))


'''
n = int(input())
i = 2
if n == 0:
    print(0)
if n == 1:
    print(1)
if n == 2:
    print(1)
else:
    a, b =  0, 1  
    for i in range(2, n+1):
        a , b = b, a+b
    print(b)
'''


