from decimal import Decimal, getcontext
getcontext().prec = 40000
def count_sixes(n):
    l=[0]*100001
    l[0]=0
    l[1]=1
    strr=['']*100001
    strr[0]='0'
    strr[1]='1'
    

    count=0
    for i in range (2,100000):
        getcontext().prec = 40000
        l[i]=(l[i-1]+l[i-2])/2
        strr[i]=str(l[i])
    x=strr[n].find('.')
    print(strr[n])
    x+=1
    ln=str(l[n])
    while(ln[x]=='6'):
        count+=1
        x+=1
    return count
print(count_sixes(10000))