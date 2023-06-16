def prime(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=1
    if s==2:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
c=0
e=0
for i in l:
    if prime(i)==1:
        c+=1
        e=e+i
v=e/c
print("%.2f"%v)