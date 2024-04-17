
def findRestaurant(list1, list2):
    dict={}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i]==list2[j]):
                dict[list1[i]]=i+j
    l=list(dict.values())
    minm=min(l) 
    result=[]
    for key,values in dict.items():
        if(values==minm):
            result.append(key)
    return result        
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))