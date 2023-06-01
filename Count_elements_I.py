m,n=map(int,input().split())
c=0
l=set(map(int,input().split()))
k=set(map(int,input().split()))
for i in l:
    for j in k:
        if i==j:
            c+=1
print(c)