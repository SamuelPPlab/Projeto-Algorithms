def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    return "".join(insertionSort(list(first_string))) == "".join(
        insertionSort(list(second_string))
    )


# Esolha Insertion Sort: Complexidade O(n^2)
# Referência: https://www.geeksforgeeks.org/insertion-sort/
# Python program for implementation of Insertion Sort
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
