def sort_list(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left, right = sort_list(lista[:mid]), sort_list(lista[mid:])
    return merge(left, right, lista.copy())


def merge(left, rigth, merged):
    left_cursor, rigth_cursor = 0, 0

    while left_cursor < len(left) and rigth_cursor < len(rigth):
        if left[left_cursor] <= rigth[rigth_cursor]:
            merged[left_cursor + rigth_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + rigth_cursor] = rigth[rigth_cursor]
            rigth_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + rigth_cursor] = left[left_cursor]

    for rigth_cursor in range(rigth_cursor, len(rigth)):
        merged[left_cursor + rigth_cursor] = rigth[rigth_cursor]

    return merged

# -------------------------------------------------------------------
# for i in range(len(lista)):
#     minimum = i
#     for j in range(i + 1, len(lista)):
#         if lista[j] < lista[minimum]:
#             minimum = j
#     lista[minimum], lista[i] = lista[i], lista[minimum]

# return lista

# -------------------------------------------------------------------

# has_swapped = True
# num_of_iterations = 0
# while has_swapped:
#     has_swapped = False

#     for index in range(len(lista) - num_of_iterations - 1):
#         if lista[index] > lista[index + 1]:
#             lista[index], lista[index + 1] = (
#                 lista[index + 1],
#                 lista[index],
#             )
#             has_swapped = True
#     num_of_iterations += 1
# return lista


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


# first_string = "ROMA"
# second_string = "AMOR"
# print(is_anagram(first_string, second_string))
