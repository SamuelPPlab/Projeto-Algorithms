def merge(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition = merge_sort(array, low, high)

        merge(array, low, partition - 1)
        merge(array, partition + 1, high)

    return array


def merge_sort(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    first_array = list(first_string)
    second_array = list(second_string)

    merge_sorted_first_array = merge(first_array, 0, len(first_array) - 1)
    merge_sorted_second_array = merge(second_array, 0, len(second_array) - 1)

    return "".join(merge_sorted_first_array) == "".join(
        merge_sorted_second_array
    )
