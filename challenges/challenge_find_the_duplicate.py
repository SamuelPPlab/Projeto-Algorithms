def find_duplicate(nums):
    for number in nums:
        if type(number) is str or number < 0:
            return False

    ordered_numbers = merge_sort(nums)
    len_ordered_numbers = len(ordered_numbers)

    for i in range(len_ordered_numbers - 1):
        if ordered_numbers[i] == ordered_numbers[i + 1]:
            return ordered_numbers[i]
    return False


# Algoritmo merge_sort do Course (Trybe)
def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right, string)


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
