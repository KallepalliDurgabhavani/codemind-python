n=int(input())
l=list(map(int,input().split()))
t=list()
a,b=map(int,input().split())
for i in range(0,n):
    if l[i]<a or l[i]>b:
        t.append(l[i])
if t:
    print(min(t))
else:
    print(-1)