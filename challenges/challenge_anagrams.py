def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for letter in first_string:
        if second_string.find(letter) != -1:
            return True
        else:
            return False
