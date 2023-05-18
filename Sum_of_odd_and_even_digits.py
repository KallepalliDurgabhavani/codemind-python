n=int(input())
e=0
o=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if(e-o==0):
    print('YES')
else:
    print('NO')
        