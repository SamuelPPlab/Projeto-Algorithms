def isValid(array):
    if isinstance(array[0], str):
        return False
    else:
        return True


def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) >= 2 and isValid(nums):
        counter = 0
        result = max(set(nums), key=nums.count)
        for index in nums:
            if index == result and index > 0:
                counter += 1
        if counter > 1:
            return result
        else:
            return False
    else:
        return False
