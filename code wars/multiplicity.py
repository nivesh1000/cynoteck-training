import math
def comp(array1, array2):
    if not array1:
        return False
    if not array2:
        return False
    if(len(array1)!=len(array2)):
        return False
    sorted1=array1.sort()
    sorted2=array2.sort()
    for i in range(len(array2)):
        if((array1[i]**2)!=array2[i]):
            return False
    return True    
print(comp([1],[1]))