def largest_element(arr):
    maximum=arr[0]
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum
print(largest_element([14,25,12,9,6]))