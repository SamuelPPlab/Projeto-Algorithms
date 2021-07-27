def find_duplicate(nums):
    for num in nums:
        if type(num) is str or num < 0:
            return False
    ordered_numbers = merge_sort(nums)
    for i in range(len(ordered_numbers) - 1):
        if ordered_numbers[i] == ordered_numbers[i + 1]:
            return ordered_numbers[i]
    return False


# Algoritmo merge_sort adaptado do course
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = len(numbers) // 2
    left, right = merge_sort(numbers[:middle]), merge_sort(numbers[middle:])
    return merge(left, right, numbers)


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged


# nums = []
# print(find_duplicate(nums))
