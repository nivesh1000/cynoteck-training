def first_non_repeating_letter(s):
    

       

    s2=s.lower()
    l=[]
    n=[]
    result=''
    for i in s:
        n.append(i)        # n contains original characters in list  
    for i in s2:
        l.append(i)         # l contains lowercase characters in list | m is the copy of lower list
    m=l.copy()
    for i in m:
        l.remove(i)
        if(i in l):
            l=m.copy()
            continue
        else:

            index=m.index(i)
            result=n[index]
            break
    return result      
        
    
            
print(first_non_repeating_letter('ssssss'))

                 
        
