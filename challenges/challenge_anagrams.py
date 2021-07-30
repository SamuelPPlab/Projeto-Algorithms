def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    list1 = list(first_string)
    list2 = list(second_string)

    if len(list1) != len(list2):
        return False

    for letter in list1:
        try:
            index = list2.index(letter)
        except ValueError:
            return False

        list2.remove(list2[index])

    return True
