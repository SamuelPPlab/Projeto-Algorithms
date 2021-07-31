def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return False

    for i in range(len(first_string)):
        if not first_string[i] in second_string:
            return False

    return True
