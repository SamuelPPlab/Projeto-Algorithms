def is_anagram(first_string, second_string):
    if (
        len(first_string) == 0
        or len(second_string) == 0
        or len(first_string) != len(second_string)
    ):
        return False
    list_first_string = []
    list_second_string = []
    for i in range(len(first_string)):
        list_first_string.append(first_string[i])
        list_second_string.append(second_string[i])

    first_string_sorted = insertion_sort(list_first_string)
    second_string_sorted = insertion_sort(list_second_string)

    if (first_string_sorted == second_string_sorted):
        return True
    return False


def insertion_sort(string_array):
    left = 0
    right = len(string_array) - 1
    for i in range(left + 1, right + 1):
        element_key = string_array[i]
        j = i - 1

        while j >= left and string_array[j] > element_key:
            string_array[j + 1] = string_array[j]
            j -= 1

        string_array[j + 1] = element_key

    return string_array
