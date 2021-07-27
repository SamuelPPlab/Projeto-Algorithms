def is_anagram(first_string, second_string):
    if not first_string:
        return False
    if not second_string:
        return False
    first_word = list(first_string)
    second_word = list(second_string)
    if len(first_word) != len(second_word):
        return False

    if insertion_sort(first_word) == insertion_sort(second_word):
        return True
    else:
        return False


def insertion_sort(array):
    for i in range(len(array)):
        value = array[i]
        position = i

        while position > 0 and array[position - 1] > value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = value
    return array
