def recoverSecret(triplets):
    s=''.join(triplets[0])
    c=0
    w=0
    loop=0
    for i in triplets:
        if(s[0]==i[1]):
            s=i[0]+s
            break
    for i in triplets:
        if(s[len(s)-1]==i[1]):
            s=s+i[2]  
            break
    while(c!=len(triplets) and w!=len(s)-1):
        print(s)
        # if(c==len(triplets) and w==len(s)-1):
        #     for i in triplets:
        #         if(s[0]==i[1]):
        #             s=s[0]+i[0]+s[1:]
        #             break
        #     for i in triplets:
        #         if(s[len(s)-1]==i[1]):
        #             s=s+i[2]  
        #             break     

        c=0
        if(c==len(triplets)):
            w+=1    
        for i in triplets:
            if(s[w]==i[0] and s[w+1]==i[2]):
                
                s=s[0]+i[1]+s[1:]
                break
            else:
                c+=1     
    loop+=1   
    return s
                
            
print(recoverSecret([  
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]))
