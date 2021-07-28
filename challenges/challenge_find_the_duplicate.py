def find_duplicate(nums):
    for numero in nums:
        if type(numero) == str or numero < 0:
            return False
        elif nums.count(num) > 1:
            return numero
    return False
