def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    sort_nums = sorted(nums)

    for index in range(1, len(sort_nums)):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False
        if sort_nums[index] == sort_nums[index - 1]:
            return sort_nums[index]

    return False
