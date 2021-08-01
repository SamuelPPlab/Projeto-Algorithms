def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    if (len(first_string) == len(second_string)):
        for character in first_string:
            index = second_string.find(character)
            if index == -1:
                return False
            else:
                second_string = second_string.replace(character, '', 1)
    else:
        return False

    return True
