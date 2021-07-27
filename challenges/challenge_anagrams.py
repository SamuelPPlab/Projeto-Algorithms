def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    for letter1 in first_string:
        for letter2 in second_string:
            if letter1 == letter2:
                return True
            else:
                return False
