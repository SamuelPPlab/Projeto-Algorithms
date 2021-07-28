
def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_count = is_sort(list(first_string))
    second_count = is_sort(list(second_string))
    if (len(first_string) != len(second_string)):
        return False
    for index in range(len(first_string)):
        if (first_count[index] != second_count[index]):
            return False
    return True


def is_sort(word):
    for i in range(len(word)):
        current_value = word[i]
        current_position = i
        
        while (
            current_position > 0
            and word[current_position - 1] > current_value
        ):
            word[current_position] = word[current_position - 1]
            current_position = current_position - 1

        word[current_position] = current_value
    return word
