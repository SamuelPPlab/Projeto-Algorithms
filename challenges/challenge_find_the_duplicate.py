from typing import Counter


def invalid_type(n):
    if type(n) == str or n < 1:
        return True
    return False


def find_duplicate(nums):
    if not nums:
        return False

    for n in nums:
        if invalid_type(n):
            return False

    most_common = Counter(nums).most_common(1)

    if most_common[0][1] >= 2:
        return most_common[0][0]
    return False
    