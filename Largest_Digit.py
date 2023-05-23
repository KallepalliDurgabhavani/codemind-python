n=int(input())
m=0
r=0
while n!=0:
    re=n%10
    if m<re:
        m=re
    n//=10
print(m)