def scramble(s1, s2):
    l1=list(s1)
    l2=list(s2)
    count=[0]*200
    for i in l1:
        count[ord(i)]+=1
    for i in l2:
        if(count[ord(i)]==0):
            return False
        else:
            count[ord(i)]-=1
    return True           
          

print(scramble('aaabbb','aac'))