def find_duplicate(nums):
    order = sorted(nums)
    for item in range(len(order)-1):
        if order[item] == order[item+1]:
            return order[item]
    return False
