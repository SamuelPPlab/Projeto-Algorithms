def sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left, right = sort(array[:mid]), sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, array):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            array[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            array[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        array[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        array[left_cursor + right_cursor] = right[right_cursor]

    return array


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_string_sorted = sort([letter for letter in first_string])
    second_string_sorted = sort([letter for letter in second_string])

    for i in range(len(first_string_sorted)):
        if first_string_sorted[i] != second_string_sorted[i]:
            return False

    return True
    