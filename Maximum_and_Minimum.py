n=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    if l.count(i)==i:
        t.append(i)
if not t:
    print(-1)
else:
    print(min(t),max(t),end=' ')