def total_sum(nums):
    s = 0
    if len(nums) == 0:
        return 0

    for n in nums:
        s += n
    return s

print(total_sum([1,2,3,4,5]))