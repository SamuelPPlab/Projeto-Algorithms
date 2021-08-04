def find_duplicate(nums):
    if not nums:
        return False
    return max(nums, key=nums.count)
