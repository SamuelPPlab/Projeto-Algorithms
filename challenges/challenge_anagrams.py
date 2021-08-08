def quicksort(some_list):
    """ Script de ordenação rápida, ref.:
            - https://wiki.python.org.br/QuickSort
    """

    if some_list:
        left = [letter for letter in some_list if letter < some_list[0]]
        right = [letter for letter in some_list if letter > some_list[0]]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [some_list[0]] * some_list.count(some_list[0]) + right
    return []


def is_anagram(first_string, second_string):
    """ Recebe duas strings e verifica se são anagramas """

    if len(first_string) == 0 or len(second_string) == 0:
        return False
    first_list = quicksort(list(first_string))
    second_list = quicksort(list(second_string))

    return first_list == second_list
