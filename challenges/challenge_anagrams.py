def sort_list(lista):
    has_swapped = True
    num_of_iterations = 0
    while has_swapped:
        has_swapped = False

        for index in range(len(lista) - num_of_iterations - 1):
            if lista[index] > lista[index + 1]:
                lista[index], lista[index + 1] = (
                    lista[index + 1],
                    lista[index],
                )
                has_swapped = True
        num_of_iterations += 1
    return lista


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False

    list_first_string = [char for char in first_string]
    list_second_string = [char for char in second_string]

    list_first_string = sort_list(list_first_string)
    list_second_string = sort_list(list_second_string)

    if list_first_string == list_second_string:
        return True

    return False
    # return list_first_string, list_second_string


# first_string = "FERNANDO"
# second_string = "FERNANDA"
# print(is_anagram(first_string, second_string))
