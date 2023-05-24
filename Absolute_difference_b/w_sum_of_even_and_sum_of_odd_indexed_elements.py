n=int(input())
s=0
o=0
l=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        s=s+l[i]
    else:
        o=o+l[i]
print(s-o)
        