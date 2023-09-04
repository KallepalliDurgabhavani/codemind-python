m=int(input())
n=int(input())
for i in range(m,n+1):
    s=0
    t=i
    while(i!=0):
        r=i%10
        s=s*10+r
        i=i//10
    if(t==s):
        print(s,end=' ')