def sort_string(list_string):
    list_result = []
    for char in list(list_string):
        for index in list_string:
            if char < index:
                list_result.append(char)
    return list_result


def is_anagram(first_string, second_string):
    if first_string != "" and second_string != "":
        if sort_string(first_string) == sort_string(second_string):
            return True
        else:
            return False
    return False
