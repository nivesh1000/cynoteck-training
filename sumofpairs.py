def sum_pairs(ints, s):
    a=-311
    b=-999
    for i in range(1,len(ints)):
        if(ints[i]<=s):
            for j in range(0,i):
                if(ints[i]<=s):
                    if(ints[i]+ints[j]==s):
                        a=ints[j]
                        b=ints[i]
                        break
                else:
                    continue
            if(a!=-311 and b!=-999):
                break
        else:
            continue    
    if(a==-311 and b==-999):
        return None
    else:
        return [a,b]
print(sum_pairs([1, 2, 3, 4, 1, 0],2))