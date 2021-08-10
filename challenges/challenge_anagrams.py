def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partitionIndex = partition(array, low, high)

        quicksort(array, low, partitionIndex - 1)
        quicksort(array, partitionIndex + 1, high)

    return array


def partition(array, low, high):
    indexPosition = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            index = index + 1
            array[index], array[j] = array[j], array[index]

    array[index + 1], array[high] = array[high], array[index + 1]

    return index + 1


def is_anagram(first_string, second_string):
    firsts = list(first_string)
    seconds = list(second_string)

    firstsSorted = quicksort(firsts, 0, len(firsts) - 1)
    secondsSorted = quicksort(seconds, 0, len(seconds) - 1)

    return "".join(firstsSorted) == "".join(secondsSorted)
