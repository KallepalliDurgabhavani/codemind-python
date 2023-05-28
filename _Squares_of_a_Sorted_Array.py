n=int(input())
l=list(map(int,input().split()))
k=list()
for i in l:
    k.append(i*i)
k.sort()
for j in k:
    print(j,end=' ')