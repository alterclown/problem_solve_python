def find_large_in_array(arr):
    maxValue = arr[0]
    for item in range(1, len(arr)):
        if arr[item] > maxValue:
            maxValue = arr[item]

    return maxValue
print(find_large_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


res = find_large_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(res)