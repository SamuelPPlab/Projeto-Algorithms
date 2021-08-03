def find_duplicate(nums):
    """ Faça o código aqui. """
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    #         False
    if len(nums) == len(set(nums)):
        return False
    return max(nums, key=nums.count)
# 4 - python3 -m pytest tests/challenge_find_the_duplicate.py
