def find_max(nums):
    m = -float("inf")
    for n in nums:
        if n > m:
            m = n
    return m

print(find_max(nums=[4, 5, 90, 43, 199, 3, 1, 23]))