def to_underscore(string):
    a=list(string)
    i=1
    while(i<len(string)):
        if a[i].isupper():
            a.insert(i,'_')
            i+=1
        i+=1
            
    
    return ''.join(a)
print(to_underscore('helloWorld'))
