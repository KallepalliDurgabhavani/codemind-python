def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
i=int(input())   
if(isPronicNumber(i)):    
    print("YES")
else:
    print("NO")
       