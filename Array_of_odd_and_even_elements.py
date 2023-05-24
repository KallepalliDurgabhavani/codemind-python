n=int(input())
l=list(map(int,input().split()))
o=list()
e=list()
for i in range(0,n):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
s=o+e
for i in range(0,n):
    print(s[i],end=' ')