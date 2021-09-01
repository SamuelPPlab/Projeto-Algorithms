def find_duplicate(nums):
    sort = sorted(nums)
    if not nums:
        return False
    for index in range(1, len(sort)):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False
        if sort[index] == sort[index - 1]:
            return sort[index]
    return False
