def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)

    if len(first_list) != len(second_list):
        return False

    for letter in first_list:
        try:
            index = second_list.index(letter)
        except ValueError:
            return False

        second_list.remove(second_list[index])

    return True


# https://www.w3schools.com/python/ref_string_find.asp
# https://www.vivaolinux.com.br/topico/Python/Verificar-existencia-de-uma-letra-em-uma-string
# https://www.geeksforgeeks.org/python-list-index/
