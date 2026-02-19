def find_max(nums):
    max = -float("inf")
    for num in nums:
        if num > max:
            max = num
    return max


# print(find_max([32,1,43,5434,12]))
