def insertion_sort(nums):
    for i in range(len(nums)):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums      

print(insertion_sort([3,54,75,1,89,6,90,2,22,4]))