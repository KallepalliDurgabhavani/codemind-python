n=int(input())
l=list(map(int,input().split()))
s=0
avg=sum(l)/n
for i in range(0,n):
    if avg>=l[i]:
        s+=1
print(s)