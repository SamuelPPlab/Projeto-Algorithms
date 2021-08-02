def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    return "".join(insertionSort(list(first_string))) == "".join(
        insertionSort(list(second_string))
    )


def insertionSort(arr):
    for item in range(1, len(arr)):
        key = arr[item]
        x = item - 1
        while x >= 0 and key < arr[x]:
            arr[x + 1] = arr[x]
            x -= 1
        arr[x + 1] = key

    return arr
