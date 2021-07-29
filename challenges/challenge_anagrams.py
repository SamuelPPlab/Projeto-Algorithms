def is_anagram(first_string, second_string):
    # return Counter(first_string) == Counter(second_string)
    if (len(first_string) != len(second_string)):
        return False
    first_dict = (
        {i: first_string.count(i) for i in first_string}
    )
    second_dict = (
        {a: second_string.count(a) for a in second_string}
    )
    return first_dict == second_dict
