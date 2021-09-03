def find_duplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    counts = [0] * len(nums)
    for num in nums:
        if num < 0:
            return False
        counts[num] += 1
        if counts[num] > 1:
            return num
    return False
