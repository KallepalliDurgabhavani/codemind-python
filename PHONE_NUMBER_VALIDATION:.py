n=int(input())
t=n
re=0
while n!=0:
    r=n%10
    re=re*10+r
    n//=10
s=re%10
p=str(t)
b=len(p)
if s!=0 and b==10:
    print("Valid")
else:
    print("Invalid")
    
        