def next_bigger(n):
    s=str(n)
    list1=list(s)
    i=len(list1)-1
    list2=[]
    while(i>0):
        if(int(list1[i])>int(list1[i-1])):
            list2.append(int(list1[i]))
            list2.sort()
            i-=1
            j=0
            while(j<len(list2)):
                if(int(list1[i])>=list2[j]):
                    j+=1
                    continue
                else:
                    temp=list1[i]
                    list1[i]=str(list2[j])
                    list2[j]=int(temp)
                    break
            break        
            
        else:
            list2.append(int(list1[i]))
            list2.sort()
            i-=1 #list2 got the after numbers in int 
    list1=list1[:i+1]
    for i in list2:
        list1.append(str(i))
    if(int(''.join(list1))>n):    
        return int(''.join(list1))    
    else:
        return -1
print(next_bigger(1990))      
           
