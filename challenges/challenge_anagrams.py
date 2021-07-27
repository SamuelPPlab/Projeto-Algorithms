def is_anagram(first_string, second_string):
    if (
        len(first_string) == 0
        or len(second_string) == 0
        or len(first_string) != len(second_string)
    ):
        return False
    first_string_sorted = sorted(first_string)
    second_string_sorted = sorted(second_string)
    if (first_string_sorted == second_string_sorted):
        return True
    return False
