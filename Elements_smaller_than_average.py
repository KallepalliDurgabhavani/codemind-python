n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
c=0
for i in range(0,n):
    if(avg>=l[i]):
        c+=1
print(c)