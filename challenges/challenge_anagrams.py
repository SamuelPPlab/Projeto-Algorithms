def sort_string(list_string):
    list_result = []
    for char in list_string:
       for index in list_string:
           if char < index:
               list_result.append(char)
    return list_result


def is_anagram(first_string, second_string):
    if first_string != "" and second_string != "":
        list_str1 = sort_string(list(first_string))
        list_str2 = sort_string(list(second_string))
        return(list_str1 == list_str2)
    return False


