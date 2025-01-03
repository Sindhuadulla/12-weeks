def maximum_consecutive_ones(arr):
    cur_sum=0 
    max_sum=0 
    for i in range(len(arr)):
        if arr[i]==1 :
            cur_sum+=1 

            if cur_sum>max_sum:
                max_sum=cur_sum 
        else:
            cur_sum=0
    return max_sum 
print(maximum_consecutive_ones([1,0,1,1,0,1,0,1,1,1,1]))