def return_duplicate_value(nums):
    """ Faça o código aqui. """
    nums.sort()
    for i in range(1, len(nums)):
        if (nums[i] == nums[i-1]):
            return nums[i]
    return False


def find_duplicate(nums):
    """ Faça o código aqui. """
    if (len(nums) == 0):
        return False

    for num in nums:
        if isinstance(num, int) is False or num < 1:
            return False
    return return_duplicate_value(nums)

    # referencia carlos8v pull #58
