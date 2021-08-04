def find_duplicate(nums):
    """ Faça o código aqui. """
    if ((len(nums) == len(set(nums))) or (len(nums) == 1)) or (nums == ''):
        return False
    # if ((nums == '') or (nums == str)):  # is the same?
        # return False
    ordered_nums = sorted(nums)
    for target in range(len(nums) - 1):  # -1 because iteration
        if ordered_nums[target] < 0:
            return False
        if ordered_nums[target] == ordered_nums[target+1]:
            dup_num = ordered_nums[target]
            return dup_num
    return False

# 4 - python3 -m pytest tests/test_find_the_duplicate.py
