def moving_zeros_to_end_of_the_array(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1 
    return arr 
print(moving_zeros_to_end_of_the_array([1,0,0,3,7,0,8,2,0]))