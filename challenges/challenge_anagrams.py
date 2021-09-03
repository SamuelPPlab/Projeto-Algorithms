def compare_to_pivot(array, i, j, pivot):
    while array[i] < pivot:
        i += 1
    while array[j] > pivot:
        j -= 1
    if i <= j:
        array[j], array[i] = array[i], array[j]
        i += 1
        j -= 1
    return i, j, array


def quicksort(array, left_idx, right_idx):
    i, j = left_idx, right_idx
    pivot = (array[i] + array[j]) / 2
    while i < j:
        i, j, array = compare_to_pivot(array, i, j, pivot)
    if left_idx < j:
        array = quicksort(array, left_idx, j)
    if right_idx > i:
        array = quicksort(array, i, right_idx)
    return array


def is_anagram(first_string, second_string):
    if '' in [first_string, second_string] or \
            len(first_string) != len(second_string):
        return False
    first_string = [ord(c) for c in first_string]
    second_string = [ord(c) for c in second_string]
    first_string_sorted = quicksort(first_string, 0, len(first_string) - 1)
    second_string_sorted = quicksort(second_string, 0, len(second_string) - 1)

    return first_string_sorted == second_string_sorted
