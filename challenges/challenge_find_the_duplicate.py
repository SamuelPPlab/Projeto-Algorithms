def find_duplicate(nums):
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if nums.count(number) >= 2:
            return number
    return False
