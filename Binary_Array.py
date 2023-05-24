n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,n):
    if l[i]==0 or l[i]==1:
        c+=1
if c==n:
    print(True)
else:
    print(False)