import math

def sum_divisor(arr,n,mid):
    sum=0 
    for i in range(n):
        sum+=math.ceil(arr[i]/mid)
    return sum




def minimum_divisor(arr,n,limit):
    max_element=max(arr)
    low=1
    high=max_element
    ans=max_element
    while (low<=high):
        mid=(low+high)//2 
        if (sum_divisor(arr,n,mid)<=limit):
            ans=mid
            high=mid-1 
        else:
            low=mid+1 
    return ans 
print(minimum_divisor([9,35,19,17,7],5,11))
