n=int(input())
l=list(map(int,input().split()))
f=0
s=0
for i in range(0,n//2):
    f=f+l[i]
for j in l:
    s=s+j
last=s-f
print(f)
print(last)