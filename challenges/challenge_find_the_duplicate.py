def find_duplicate(nums):
    test = dict()
    results = False

    for num in nums:
        if not isinstance(num, int) or num < 0:
            results = False
            break
        elif bool(test.get(num, 0)):
            results = num
            break

        test[num] = 1

    return results