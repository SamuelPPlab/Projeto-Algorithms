def check_value(value):
    if (type(value) is not int) or (value < 0):
        return False
    return True


def find_duplicate(nums):
    """ Faça o código aqui. """
    list_doubles = []
    nums_support = nums.copy()
    if (len(nums) == 0):
        return False

    for i in nums:
        del(nums_support[0])

        if check_value(i) and (i in nums_support):
            list_doubles.append(i)

    if len(list_doubles) == 0:
        return False

    return list_doubles[0]
