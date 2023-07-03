n,k,m=map(int,input().split())
s=k*m
if n%s==0:
    print(int(n/s))
else:
    print(int((n/s)+1))