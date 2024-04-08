def sum_dig_pow(a,b):
    result=[]
    for i in range (a,b+1):
        s=str(i)
        l=1
        sum=0
        for j in s:
            j=int(j)
            sum+=j**l
            l+=1
        if(sum==i):
            result.append(i)
    print(result) 
sum_dig_pow(1,1000)      