def find_duplicate(nums):
    if len(nums) <= 1 or any(type(num) is str or num < 0 for num in nums):
        return False

    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    if all(value == 1 for value in count_dict.values()):
        return False

    return max(count_dict, key=count_dict.get)
