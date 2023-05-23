n=int(input())
e=list()
o=list()
l=list(map(int,input().split()))
for i in range(0,n):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
s=e+o
for j in s:
    print(j,end=' ')
