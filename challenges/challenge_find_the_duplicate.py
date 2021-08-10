def find_duplicate(nums):
    """ Faça o código aqui. """
    list_doubles = []
    nums_support = nums.copy()
    try:
        if (len(nums) == 0):
            return False

        for index, i in enumerate(nums):
            del(nums_support[0])
            if (type(i) is not int) or (i < 0):
                return False
            if i in nums_support:
                list_doubles.append(i)

        if len(list_doubles) == 0:
            return False

        return list_doubles[0]
    except TypeError:
        return False
