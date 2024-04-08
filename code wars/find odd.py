def find_it(seq):
    for i in seq:
        if(seq.count(i)%2==1):
            print(i)
find_it([1,2,3,4,1,2,3,4,5])            