def next_bigger(n):
    s=str(n)
    s=s[::-1]
    
    for i in range(len(s)):
        if(int(s[i])>int(s[i+1])):
            temp=s[i]
            s[i]=s[i+1]
            s[i+1]=temp
            break
    return int(s[::-1])  
print(next_bigger(1990))      
           
