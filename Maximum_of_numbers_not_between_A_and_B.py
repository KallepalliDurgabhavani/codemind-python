n=int(input())
l=list(map(int,input().split()))
m,n=map(int,input().split())
e=[]
for i in l:
    if i<m or i>n:
        e.append(i)
if e:
    print(max(e))
else:
    print(-1)
    
        