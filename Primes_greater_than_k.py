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
k=int(input())
c=0
for i in l:
    if i>=k and prime(i)==1:
        c+=1
print(c)