def ceil(arr,n,m):
    low,high,ans=0,n-1,n

    while low<=high :
        mid=(low+high)//2 
        if arr[mid]>=m:
            ans=arr[mid]
            high=mid-1 

        else:
            low=mid+1 
    return ans 
print(ceil([1,2,6,7],4,5))

def floor(arr,n,m):
    low,high,ans=0,n-1,n

    while low<=high :
        mid=(low+high)//2 
        if arr[mid]<=m:
            ans=arr[mid]
            low=mid+1

        else:
            high=mid-1
    return ans 
print(floor([1,2,6,7],4,5))