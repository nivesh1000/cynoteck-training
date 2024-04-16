def increment_string(strng):
    if(len(strng)==0):
        return '1'
    dig=''
    i=0
    for i in range(len(strng)-1,-1,-1):
        if(strng[i].isdigit()):
            continue
        else:
            break
    
    if(strng[i].isdigit()):
        dig=strng
        strng=''   
    else:
        dig=strng[i+1:len(strng)+1]
        strng=strng[0:i+1]
    # print(i)
    # print(dig)
    # print(strng)
    if(len(dig)==0):
        return strng+'1'
    else:
        zero=''
        i=''
        for i in range(len(dig)):
            if(dig[i]!='0' or i==len(dig)-1):
                break
            else:
                zero+=dig[i]
        dig2=dig[i:len(dig)]

        dig3=int(dig2)
        dig3+=1
        if(len(zero)>0 and len(str(dig2))<len(str(dig3))):
            zero=zero[0:len(zero)-1]

    
    return strng+zero+str(dig3)
print(increment_string('e203741000000060826439'))   