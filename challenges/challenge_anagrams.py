def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_list = list(first_string)
    second_list = list(second_string)

    for letter in first_list:
        if letter in second_list:
            second_list.remove(letter)
    return len(second_list) == 0

# Referência: Carol Andrade
