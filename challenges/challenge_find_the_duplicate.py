def find_duplicate(nums):
    repeated_num = False

    for num in nums:
        if not isinstance(num, int) or num < 1:
            return repeated_num
        storage = (num, nums.count(num))
        if storage[1] > 1:
            repeated_num = num
            return repeated_num
    return repeated_num
