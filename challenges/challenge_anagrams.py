def is_anagram(first_string, second_string):
    first_string = list(first_string)
    second_string = list(second_string)

    if len(first_string) != len(second_string):
        return False

    j = len(second_string) - 1
    for i in range(len(first_string)):
        if(second_string[j] != first_string[i]):
            return False
        j = j - 1

    return True
