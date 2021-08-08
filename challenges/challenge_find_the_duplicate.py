def find_duplicate(nums):
    iterations = []

    if not nums:
        return False

    for num in nums:
        if str(num) == num or num < 0:
            return False

        elif num in iterations:
            return num

        iterations.append(num)

    return False
