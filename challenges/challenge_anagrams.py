def is_anagram(first_string, second_string):
    len_str1 = len(first_string)
    len_str2 = len(second_string)

    if first_string == '' or second_string == '' or len_str1 != len_str2:
        return False

    first_str_ordered = merge_sort(list(first_string))
    second_str_ordered = merge_sort(list(second_string))

    if first_str_ordered == second_str_ordered:
        return True
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
