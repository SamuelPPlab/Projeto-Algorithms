def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)
    first_list.sort()
    second_list.sort()
    return first_list == second_list
