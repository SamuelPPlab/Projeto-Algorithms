def find_duplicate(nums):

    ocureences = dict()
    results = False

    for num in nums:
        if not isinstance(num, int) or num < 0:
            results = False
            break
        elif bool(ocureences.get(num, 0)):
            results = num
            break

        ocureences[num] = 1

    return results
