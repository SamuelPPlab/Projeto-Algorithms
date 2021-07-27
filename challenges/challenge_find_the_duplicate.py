def find_duplicate(nums):
    if len(nums) < 2:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if (
            nums[i] == nums[i + 1]
            and isinstance(nums[i], int)
            and nums[i] >= 0
        ):
            return nums[i]
    return False
