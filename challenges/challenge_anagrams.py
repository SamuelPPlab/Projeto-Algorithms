def sort_string(first_string):
    string_array = list(first_string)

    # Selection Sort
    for i in range(len(string_array)):
        min = i

        for j in range(i + 1, len(string_array)):
            if string_array[j] < string_array[min]:
                min = j

        string_array[min], string_array[i] = string_array[i], string_array[min]

    return string_array


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string_sorted = sort_string(first_string)
    second_string_sorted = sort_string(second_string)
    return first_string_sorted == second_string_sorted

# Aula 36.3 Trybe
