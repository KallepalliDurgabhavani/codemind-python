n=int(input())
e=0
o=0
c=0
while n!=0:
    c+=1
    re=n%10
    if re%2==0:
        e+=1
    else:
        o+=1
    n//=10
if e==c:
    print('Even')
elif o==c:
    print('Odd')
else:
    print('Mixed')
        