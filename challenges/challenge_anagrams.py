def is_anagram(first_string, second_string):
    # check if the first string and the second string is anagram
    if len(first_string) != len(second_string):
        return False
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string_list = list(first_string)
    second_string_list = list(second_string)

    if first_string_list == second_string_list:
        return True
    else:
        return False
