def find_duplicate(numbers):
    if len(numbers) <= 1:
        return False
    if not numbers:
        return False
    for number in numbers:
        if type(number) != int or number < 0:
            return False
    count = max(numbers, key=numbers.count)
    return count
