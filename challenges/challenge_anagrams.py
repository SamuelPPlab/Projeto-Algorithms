def is_anagram(first_string, second_string):
    first_result = selection_sort(list(first_string))
    second_result = selection_sort(list(second_string))

    return first_result == second_result


def selection_sort(string):
    for i in range(len(string)):
        minimum = i
        for j in range(i + 1, len(string)):
            if string[j] < string[minimum]:
                minimum = j
        string[minimum], string[i] = string[i], string[minimum]

    return string
