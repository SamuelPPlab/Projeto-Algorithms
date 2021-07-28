def find_duplicate(nums):
    nums_size = len(nums)
    if nums_size <= 1:
        return False

    for index in range(nums_size):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False
        new_index = nums[index] % nums_size
        nums[new_index] = nums[new_index] + nums_size
        if nums[new_index] > nums_size * 2:
            return new_index
    return False
