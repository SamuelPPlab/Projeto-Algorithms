def sort_string(list_string):
    for index in range(len(list_string)):
        current_char = list_string[index]
        while index > 0 and list_string[index - 1] > current_char:
            list_string[index] = list_string[index - 1]
            index -= 1
        list_string[index] = current_char
    return list_string
    


def is_anagram(first_string, second_string):
    if first_string != "" or second_string != "": 
        list_str1 = sort_string(list(first_string))
        list_str2 = sort_string(list(second_string))
        return(list_str1 == list_str2)
    return False
