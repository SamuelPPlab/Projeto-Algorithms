def count_nums(list_nums, initial_index, last_index):
    if list_nums[last_index]["n"] < 0:
        raise ValueError
    elif len(list_nums) < 2:
        return False
    elif last_index == -1:
        return list_nums
    else:
        if list_nums[initial_index]["n"] == list_nums[last_index]["n"]:
            list_nums[initial_index]["count"] += 1
        return count_nums(list_nums, initial_index, last_index - 1)


def higher_num(list_nums):
    initial_num = list_nums[0]
    initial_num["not_unique"] = False

    for num in list_nums:
        if (
            num["n"] != initial_num["n"]
            and num["count"] == initial_num["count"]
        ):
            initial_num["not_unique"] = True
        elif (
            num["n"] != initial_num["n"]
            and num["count"] > initial_num["count"]
        ):
            initial_num = num
            initial_num["not_unique"] = False

    if initial_num["not_unique"] is True:
        return False
    return initial_num["n"]


def find_duplicate(nums):
    try:
        list_nums = [{"n": int(n), "count": 0} for n in nums]
        length = len(nums)

        for n in range(length):
            list_nums = count_nums(list_nums, n, length - 1)

        return higher_num(list_nums)
    except Exception:
        return False


if __name__ == "__main__":
    nums = ["a", "b", "a"]
    print(find_duplicate(nums))
    # saída: False

    nums = [2, 2, -1]
    print(find_duplicate(nums))
    # saída: False

    nums = [1, 2, 2, 1]
    print(find_duplicate(nums))
    # saída: False

    nums = [3, 1, 3, 4, 2]
    print(find_duplicate(nums))
    # # saída: 3

    nums = [1]
    print(find_duplicate(nums))
    # # saída: 1

    nums = [1, 1, 2]
    print(find_duplicate(nums))
    # # saída: 1

    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    print(find_duplicate(nums))
    # saída: 7
