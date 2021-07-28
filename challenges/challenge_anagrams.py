def is_anagram(first_string, second_string):
    first = list(first_string)
    second = list(second_string)
    list1_length = len(first)
    list2_length = len(second)

    if list1_length != list2_length or list1_length == 0 or list2_length == 0:
        return False

    sorted_list1 = quicksort(first, 0, list1_length - 1)
    sorted_list2 = quicksort(second, 0, list2_length - 1)
    bol = True
    for index in range(list1_length):
        if sorted_list1[index] != sorted_list2[index]:
            bol = False
    return bol


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
