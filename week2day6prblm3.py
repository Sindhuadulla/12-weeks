def power(mid,n):
    prod=1 
    for i in range(n):
        prod=prod*mid
    return prod  


def nth_root_m(n,m):
    low=0
    high=m
    ans=0
    while(low<=high):
        mid=(low+high)//2 
        if (power(mid,n)==m):
            return mid
        elif power(mid,n)<m:
            low=mid+1 
        else:
            high=mid-1 
    return -1 
print(nth_root_m(2,64))
        
