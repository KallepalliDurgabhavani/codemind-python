n=int(input())
l=list(map(int,input().split()))
t=list()
a,b=map(int,input().split())
for i in range(0,n):
    if l[i]>=a and l[i]<=b:
        t.append(l[i])

print(sum(t))
