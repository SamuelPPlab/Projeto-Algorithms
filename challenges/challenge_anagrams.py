def is_anagram(first_string, second_string):
    for item in first_string:
        lista = [letter == item for letter in second_string]
    if (
        len(lista) == len(first_string)
        and first_string != ""
        and second_string != ""
    ):
        return True
    return False
