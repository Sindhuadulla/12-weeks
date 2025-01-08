def serach_insert_at_position(arr,n,m):
    low,high,ans=0,n-1,n

    while low<=high :
        mid=(low+high)//2 
        if arr[mid]>=m:
            ans=mid
            high=mid-1 

        else:
            low=mid+1 
    return ans 
print(serach_insert_at_position([1,2,6,7],4,5))
