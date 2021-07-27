def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    count_dict = {}
    for num in nums:
        if type(num) is str or num < 0:
            return False
        elif num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return max(count_dict, key=count_dict.get)
