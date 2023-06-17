def num(n):
    r=0
    while(n!=0):
        s=n%10
        r=r+s
        n//=10
    return r
n=int(input())
w=0
l=list(map(int,input().split()))
for i in l:
    w=w+num(i)
print(w)