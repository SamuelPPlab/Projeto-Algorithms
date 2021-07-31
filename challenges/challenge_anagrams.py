def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)

    return array


def partition(array, low, high):
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

    sorted_first_array = quicksort(first_array, 0, len(first_array) - 1)
    sorted_second_array = quicksort(second_array, 0, len(second_array) - 1)

    return "".join(sorted_first_array) == "".join(sorted_second_array)
