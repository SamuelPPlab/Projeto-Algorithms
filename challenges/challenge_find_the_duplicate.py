def find_duplicate(nums):
    for item in nums:
        if type(item) == str or item < 0:
            return False
        else:
            nums.count(item) > 1
            return item
    return False
