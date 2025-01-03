def union_of_two_sorted_arrays(arr1,arr2):
    i,j=0,0 
    ans=[] 

    while (i<len(arr1) and j<len(arr2)):
        if arr1[i]<=arr2[j]:
            if not ans or arr1[i]!=ans[-1] :
                ans.append(arr1[i])
            i+=1 
        else:
            if not ans or arr2[j]!=ans[-1]:
                ans.append(arr2[j])
            j+=1
    while i<len(arr1):
        if not ans or arr1[i]!=ans[-1] :
            ans.append(arr1[i])
        i+=1
        
    while j<len(arr2):
        if not ans or arr2[j]!=ans[-1]:
            ans.append(arr2[j])
        j+=1 
    return ans 

print(union_of_two_sorted_arrays([3,3,4,5,5,6],[4,5,6,6,7,8]))


