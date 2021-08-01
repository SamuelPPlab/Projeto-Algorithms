def sort_this_string(string):
    array_string = list(string)
    for i in range(len(array_string)):
        current_value = array_string[i]
        current_position = i
        while (
            current_position > 0
            and array_string[current_position - 1] > current_value
        ):
            array_string[current_position] = array_string[current_position - 1]
            current_position = current_position - 1
        array_string[current_position] = current_value
    return array_string


def is_anagram(first_string, second_string):
    if(len(first_string) < 1
    or len(second_string) < 1):
        return False
    return sort_this_string(first_string) == sort_this_string(second_string)
