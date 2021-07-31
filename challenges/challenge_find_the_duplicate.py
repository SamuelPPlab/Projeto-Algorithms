def return_duplicated_value(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if (nums[i] == nums[i-1]):
            return nums[i]

    return False


def find_duplicate(nums):
    if (len(nums) == 0):
        return False

    for num in nums:
        if isinstance(num, int) is False or num < 1:
            return False

    return return_duplicated_value(nums)
