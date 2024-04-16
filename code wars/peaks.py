def pick_peaks(arr):
    peak=[]
    pos=[]
    for i in range(1,len(arr)-1):
        if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            peak.append(arr[i])
            pos.append(i)
        elif(arr[i]>arr[i-1] and arr[i]>=arr[i+1]):   
            
            for j in range(i,len(arr)):
                if(arr[i]>arr[j]):

                    peak.append(arr[i])
                    pos.append(i)
                    break
                elif(arr[i]<arr[j]):
                    break
                else:
                    continue
                       
    dict={}
    dict["pos"]=pos
    dict["peaks"]=peak
    return dict

print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))    
