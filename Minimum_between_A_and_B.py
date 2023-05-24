n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=list()
for i in range(0,n):
    if l[i]>=a and l[i]<=b:
        s.append(l[i])
if (s):
    print(min(s))
else:
    print(-1)
        