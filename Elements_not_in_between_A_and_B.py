n=int(input())
l=list(map(int,input().split()))
m,n=map(int,input().split())
a=[]
for i in l:
    if i<m or i>n:
        a.append(i)
if a:
    for j in a:
        print(j,end=' ')
else:
    print(-1)