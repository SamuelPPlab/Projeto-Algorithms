def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) < 2:
        return False
    for n in nums:
        if not isinstance(n, int) or n < 1:
            return False
        count_duplicate = nums.count(n)
        if count_duplicate > 1:
            return n
    return False
