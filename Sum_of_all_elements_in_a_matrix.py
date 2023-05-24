m,n=map(int,input().split())
s=0
for i in range(0,m):
    l=list(map(int,input().split()))
    s=s+sum(l)
print(s)