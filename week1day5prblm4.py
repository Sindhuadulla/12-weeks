def single_element(arr):
    m={}

    for i in arr:
        if i in m:
            m[i]+=1 
        else:
            m[i]=1 

    for key,value in m.items():
        if value==1 :
            return key 
        
    return -1 
print(single_element([1,2,2,4,3,1,5,3,4]))