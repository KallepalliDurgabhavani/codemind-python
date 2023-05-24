n=int(input())
t=0
l=list(map(int,input().split()))
for i in range(0,n):
    if i%2!=0 and l[i]%2==0:
        t=1
        break
if t==0:
    print(True)
else:
    print(False)