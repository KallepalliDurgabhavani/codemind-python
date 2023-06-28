s=input()
v=input()
vowel='aeiouAEIOU'
c=0
for i in range(len(s)):
    if s[i]==v:
        print("True")
        print(i)
        break
else:
    print("False")
        
    