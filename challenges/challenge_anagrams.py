# def is_anagram(first_string, second_string):
#     """ Faça o código aqui. """
#     if ((first_string == '') or (second_string == '')):
#         return False
#     if(len(first_string) != len(second_string)):
#         return False
#     for index in range(len(first_string)):
#         substring = first_string[index]
#         count_in_first = first_string.count(substring)
#         count_in_second = second_string.count(substring)
#         if(count_in_first != count_in_second):
#             return False
#     return True

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if ((first_string == '') or (second_string == '')):
        return False

    for index in range(len(first_string)):

        if(second_string.count(first_string[index]) !=
           first_string.count(first_string[index])):
            return False
    return True
