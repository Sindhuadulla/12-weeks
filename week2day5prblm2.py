def maximum_sum_subarray(arr):
    resStart=0 
    resEnd=0 

    curstart=0 

    maxEnding=arr[0]

    maxSum=arr[0]

    for i in range(1,len(arr)):
        if maxEnding+arr[i]<arr[i]:
            maxEnding=arr[i]
            curstart=i 
        else:
            maxEnding+=arr[i]
        if maxEnding>maxSum:
            maxSum=maxEnding 
            resStart=curstart
            resEnd=i 

    res=arr[resStart:resEnd+1]
    return res 
print(maximum_sum_subarray([2,3,-8,7,-1,2,3]))
