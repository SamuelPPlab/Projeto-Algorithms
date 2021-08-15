from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_string_sorted = merge_sort(first_string)
    second_string_sorted = merge_sort(second_string)
    return first_string_sorted == second_string_sorted
