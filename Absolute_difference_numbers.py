n,x=map(int,input().split())
f=10**x
first=n%f
l=str(n)
la=l[:x]
last=int(la)
if first>last:
    print(first-last)
else:
    print(last-first)