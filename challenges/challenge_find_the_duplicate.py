def find_duplicate(nums):
    if nums == []:
        return False
    order = sorted(nums)
    if type(order[0]) == str or order[0] < 0:
        return False
    for item in range(len(order)-1):
        if type(order[item]) == str:
            return False
        if order[item] == order[item+1]:
            return order[item]
    return False


print(find_duplicate(["a", "b"]))
