def duplicate_value(nums):
    nums.sort()
    for index in range(1, len(nums)):
        if (nums[index] == nums[index-1]):
            return nums[index]

    return False


def find_duplicate(nums):
    if (len(nums) == 0):
        return False

    for num in nums:
        if isinstance(num, int) is False or num < 1:
            return False

    return duplicate_value(nums)
