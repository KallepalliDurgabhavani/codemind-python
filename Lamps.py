n,k,x,y=map(int,input().split())
r=k*x
p=n-k
s=p*y
if x>y:
    print(r+s)
else:
    print(r+(p*x))