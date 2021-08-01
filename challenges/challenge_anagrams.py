def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    arr_second_string = list(second_string)
    copy_arr_second_string = arr_second_string.copy()
    for i in range(len(first_string)):
        if first_string[i] not in copy_arr_second_string:
            return False
        else:
            arr_second_string[i] = first_string[i]
            copy_arr_second_string.remove(first_string[i])
    if first_string == ''.join(arr_second_string):
        return True
    else:
        return False
