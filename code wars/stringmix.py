def mix(s1, s2):
    dict1={}
    dict2={}
    l2=[]
    result=''
    for i in range(97,123):
        dict1[i]=''
    for i in range(97,123):
        dict2[i]=''   
    for i in s1:
        if i.islower():
            dict1[ord(i)]+=i
    for i in s2:
        if i.islower():
            dict2[ord(i)]+=i 
    maxx=0        
    for i in range(97,123):
        if(len(dict1[i])>len(dict2[i]) and len(dict1[i])>1):
            l2.append(('1',dict1[i]))
            maxx=max(maxx,len(dict1[i]))
        elif(len(dict1[i])<len(dict2[i]) and len(dict2[i])>1):
            l2.append(('2',dict2[i]))
            maxx=max(maxx,len(dict2[i]))    
        elif((len(dict1[i])==len(dict2[i])) and len(dict2[i])>1):
            l2.append(('=',dict1[i]))
            maxx=max(maxx,len(dict1[i]))
       
    while(maxx>1):
        for i in l2:
            if(len(i[1])==maxx and i[0]=='1'):
                result=result+i[0]+':'+i[1]+'/'
        for i in l2:
            if(len(i[1])==maxx and i[0]=='2'):
                result=result+i[0]+':'+i[1]+'/'  
        for i in l2:
            if(len(i[1])==maxx and i[0]=='='):
                result=result+i[0]+':'+i[1]+'/'              
        maxx-=1
    return result[:len(result)-1]
print(mix("my&friend&Paul has heavy hats! &","my friend John has many many friends &"))