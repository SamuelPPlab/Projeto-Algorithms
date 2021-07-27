# codigo do course
def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array


def is_anagram(first_string, second_string):
    first_string_ordered = ''.join(selection_sort(list(first_string)))
    second_string_ordered = ''.join(selection_sort(list(second_string)))

    if first_string_ordered == second_string_ordered:
        return True

    return False
