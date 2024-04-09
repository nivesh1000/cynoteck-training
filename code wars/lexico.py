def in_array(array1, array2):
    array3=[]
    for i in range(len(array1)):
        for j in range(len(array2)):
            if(array1[i] in array2[j] and array1[i] not in array3):
                array3.append(array1[i])
                # print(array3)
    array3.sort()
    return array3
    # print(array3)
in_array(["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"])    