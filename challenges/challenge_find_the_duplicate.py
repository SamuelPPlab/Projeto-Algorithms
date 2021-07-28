def find_duplicate(nums):
    """ Faça o código aqui. """
    repeated = ''
    sorted(nums)
    if (len(nums) <= 1):
        return False

    for number in nums:
        if nums.count(number) > 1:
            repeated = number
            instance = isinstance(number, str)

    if (repeated is not None or instance is True):
        return repeated
    else:
        return False
