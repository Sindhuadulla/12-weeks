def binarysearchiteration(arr,n,target):
    low=0
    high=n-1
    

    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target :
            return mid 
        elif arr[mid]<target:
            low=mid+1 
        else:
            high=mid-1 
    return -1 
print(binarysearchiteration([1,2,3,4,5],5,4))

def recursive_approach(arr,low,high,target):
    
    if low>high:
        return -1 
    mid=(low+high)//2 
    if arr[mid]==target:
        return mid 
    elif arr[mid]<arr[target]:
        return recursive_approach(arr,mid+1,high,target)
    else:
        return recursive_approach(arr,low,mid-1,target)
print(recursive_approach([1,2,3,4,5],0,4,4))

        