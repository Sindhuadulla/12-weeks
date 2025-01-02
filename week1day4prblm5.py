def left_rotate_by_1_place(arr,n):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp

    return arr 
print(left_rotate_by_1_place([1,2,3,4,5],5))

def left_rotate_by_k_places(arr,n,k):
    temp=arr[:k]
    arr[:n-k]=arr[k:]
    arr[n-k:]=temp 
    return arr 
print(left_rotate_by_k_places([1,2,3,4,5],5,3))