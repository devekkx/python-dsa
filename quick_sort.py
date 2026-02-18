def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low 
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

nums = [64, 34, 25, 12, 22, 11, 90]
quick_sort(nums, 0, len(nums)-1)
print(nums) 