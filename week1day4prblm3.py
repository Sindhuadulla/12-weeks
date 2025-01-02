def array_is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False 
    return True 
print(array_is_sorted([23,14,56,78]))

def removing_duplicates(arr,N):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1 
           
    return i+1,arr

unique_count=removing_duplicates([3,3,5,5,7,7],6)
print(unique_count)    


def remove_duplicates(a, n):
    s = set()
    for i in range(n):
        s.add(a[i])
    j = 0
    for k in s:
        a[j] = k
        j += 1
    return len(s),a ,s

unique_count=remove_duplicates([3,3,5,5,7,7],6)
print(unique_count)    
