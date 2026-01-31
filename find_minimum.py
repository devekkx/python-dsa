def find_minimum(nums):
    if len(nums) ==0:
        return None

    minn = float("inf")
    for num in nums:
        if num < minn:
            minn = num
    return minn

print(find_minimum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_minimum([]))