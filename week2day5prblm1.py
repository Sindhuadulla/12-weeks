def maximum_subarray(arr):
    maxEnding=arr[0]
    res=arr[0]

    for i in range(1,len(arr)):

        maxEnding=max(maxEnding+arr[i],arr[i])

        res=max(maxEnding,res) 
    return res 
print(maximum_subarray([2,3,-8,7,-1,2,3]))