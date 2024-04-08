def sort_array(source_array):
    for i in range(len(source_array)):
        for j in range (i+1,len(source_array)):    
            if(source_array[i]%2==1 and source_array[j]%2==1 and source_array[i]>source_array[j]):
                temp=source_array[j]
                source_array[j]=source_array[i]
                source_array[i]=temp
    return source_array        
    print(source_array)          
sort_array([11, 1, 2, 8, 3, 4, 5])


