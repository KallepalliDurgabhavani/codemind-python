n=int(input())
l=list(map(int,input().split()))
c=0
s=set(l)
for i in s:
    if l.count(i)==i:
        c+=1
print(c)