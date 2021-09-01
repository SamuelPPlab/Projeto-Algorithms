def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for index in first_string:
        if second_string.find(index) != -1:
            return True
        else:
            return False
