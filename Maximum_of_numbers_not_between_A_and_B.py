n=int(input())
a=list()
l=list(map(int,input().split()))
p,m=map(int,input().split())
for i in range(0,n):
    if l[i]<p or l[i]>m:
        a.append(l[i])
if a:
    print(max(a))
else:
    print(-1)