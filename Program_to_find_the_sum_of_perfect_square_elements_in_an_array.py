def sq(n):
    s=int(n**0.5)
    if s*s==n:
        return 1
    else:
        return 0
n=int(input())
s=0
l=list(map(int,input().split()))
for i in l:
    if sq(i):
        s=s+i
print(s)
