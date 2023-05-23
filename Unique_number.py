n=int(input())
l=list()
x=n
while n>0:
    rem=n%10
    l.append(rem)
    n=n//10
for ele in l:
    if l.count(ele)>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")