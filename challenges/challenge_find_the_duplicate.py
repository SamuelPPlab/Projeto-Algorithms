def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) > 2:
        result = max(set(nums), key=nums.count)
        if result != 1:
            return result
        else:
            return False
    return False
