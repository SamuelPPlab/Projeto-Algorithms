def find_duplicate(nums):

    results = False
    searchs = dict()

    for num in nums:
        if not isinstance(num, int) or num < 0:
            results = False
            break
        elif bool(searchs.get(num, 0)):
            results = num
            break

        searchs[num] = 1

    return results
