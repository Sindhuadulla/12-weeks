def second_largest(arr):
    first_max=0
    second_max=-1
    for i in range(len(arr)):
        if arr[i]>first_max:
            second_max=first_max
            first_max=arr[i]
        if arr[i]>second_max and arr[i]!=first_max:
            second_max=arr[i]
    return second_max 
print(second_largest([23,16,18,5,45]))