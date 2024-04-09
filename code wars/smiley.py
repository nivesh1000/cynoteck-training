def count_smileys(arr):
    c=0
    for i in arr:
        if(len(i)==2):
            if((i[0]==';' or i[0]==':') and (i[-1]==')' or i[-1]=='D')):
                c+=1
        if(len(i)==3):
            if((i[0]==';' or i[0]==':') and (i[-1]==')' or i[-1]=='D')and(i[1]=='-' or i[1]=='~')):
                c+=1        

    return c        
            