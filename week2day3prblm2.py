def lower_bound(arr,x,N):
    low,high,ans=0,N-1,N
    while low<=high :
        mid=(low+high)//2 
        if arr[mid]>=x:
            ans=mid
            high=mid-1 
        else:
            low=mid+1 
    return ans 
print(lower_bound([2,3,4,5,8],8,5))

def upper_bound(arr,x,N):
    low,high,ans=0,N-1,N
    while low<=high :
        mid=(low+high)//2 
        if arr[mid]>x:
            ans=mid
            high=mid-1 
        else:
            low=mid+1 
    return ans 
print(upper_bound([2,3,4,5,8],8,5))
