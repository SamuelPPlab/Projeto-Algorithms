def is_anagram(first_string, second_string):
    first_ordered = merge_sort(list(first_string))
    second_ordered = merge_sort(list(second_string))
    if first_ordered == second_ordered:
        return True
    return False


# Segunda Tentativa -> Algoritmo merge_sort adaptado do course
def merge_sort(string):
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left, right = merge_sort(string[:middle]), merge_sort(string[middle:])
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


# first_word = 'PEDARA'
# second_word = 'PERDAA'
# print(is_anagram(first_word, second_word))

# Primeira tentativa -> excedeu o tempo
# def selection_sort(array):
#     if len(array) <= 1:
#         return array
#     for i in range(len(array)):
#         minimum = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[minimum]:
#                 minimum = j
#         array[minimum], array[i] = array[i], array[minimum]
#     return array
