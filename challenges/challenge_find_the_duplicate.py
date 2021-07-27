def find_duplicate(nums):
    nums.sort()
    for (index, number) in enumerate(nums[:-1]):
        if not isinstance(number, int) or number < 0:
            return False
        if number == nums[index + 1]:
            return number
    return False


nu = [1, 3, 4, 2]
print(find_duplicate(nu))
