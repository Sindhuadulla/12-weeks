#using linearsearch 
def peak_element(arr,n):
    if n==0:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1 
    for i in range(n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1] :
            return arr[i]
    return -1 
print(peak_element([1, 2, 3 ,4 ,5, 6, 7, 8, 4, 2, 1],11))

#using binary search
def find_peak_element(arr,N):
    if N==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[N-1]>arr[N-1]:
        return N-1 
    low=0
    high=N-1 
    while low<=high :
        mid  =low+high //2 
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid] 
        if arr[mid]>arr[mid-1]:
            low = mid+1 
        else:
            high=mid-1 
    return -1
print(find_peak_element([1,2,1,4,3],5))