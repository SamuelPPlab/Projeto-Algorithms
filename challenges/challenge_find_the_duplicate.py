def find_duplicate(nums):
    """ Retorna o número duplicado da lista. """
    nums.sort()
    previous_number = 0
    for number in nums:
        if(type(number) != int or number < 1):
            return False
        if(previous_number == number):
            return number
        previous_number = number
    return False
