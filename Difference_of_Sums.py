n=int(input())
s=0
e=0
p=0
for i in range(1,n+1):
    p=p+i
    s=s+(i*i)
sum=p**2
print(abs(sum-s))