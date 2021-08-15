def find_duplicate(numbers):
    if len(numbers) <= 1:
        return False
    if not numbers:
        return False
    for number in numbers:
        if type(number) != int or number < 0:
            return False
    num = max(numbers, key=numbers.count)
    return False if numbers.count(num) <= 1 else num
