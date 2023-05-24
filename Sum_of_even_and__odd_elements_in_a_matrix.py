m,n=map(int,input().split())
s=0
o=0
for i in range(0,m):
    l=list(map(int,input().split()))
    for i in l:
        if i%2==0:
            s=s+i
        else:
            o=o+i
print(s,o)