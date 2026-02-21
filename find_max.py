def find_max(nums):
    maxx = -float("inf")
    for num in nums:
        if num > maxx:
            maxx = num
    return maxx


print(find_max([32, 1, 43, 5434, 12]))
