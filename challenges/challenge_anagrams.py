def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    list_first_string = []
    list_second_string = []
    for i in range(len(first_string)):
        list_first_string.append(first_string[i])
        list_second_string.append(second_string[i])

    first_order = ordenador(list_first_string)
    second_order = ordenador(list_second_string)
    
    if first_order == second_order:
        return True

    return False


def ordenador(word):
    left = 0
    right = len(word) - 1
    for i in range(left + 1, right + 1):
        element_key = word[i]
        j = i - 1
        while j >= left and word[j] > element_key:
            word[j + 1] = word[j]
            j -= 1
        word[j + 1] = element_key
    return word