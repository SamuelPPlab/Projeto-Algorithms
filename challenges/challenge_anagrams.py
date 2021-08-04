from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    first_list = list(first_string)
    second_list = list(second_string)

    if merge_sort(first_list) == merge_sort(second_list):
        return True

    return False
