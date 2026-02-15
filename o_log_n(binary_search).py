def binary_search(target, arr):
    low, high = 0, len(arr) -1

    while low <= high:
        median = (low + high)
        if arr[median] == target:
            return True
        if arr[median] < target:
            low = median + 1
            continue
        high = median - 1
    return False 



print(binary_search(target=3, arr=[4, 1, 5, 23, 3, 67, 2, 78]))