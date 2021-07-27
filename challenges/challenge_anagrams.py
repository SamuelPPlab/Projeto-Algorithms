def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if ((first_string == '') or (second_string == '')):
        return False
    if(len(first_string) != len(second_string)):
        return False
    for index in range(len(first_string)):
        # print(first_string[index])
        # print(second_string.find(first_string[index]))
        if(second_string.find(first_string[index]) < 0):
            return False
    return True


# if (__name__ == '__main__'):
#     first_string = "coxinha"
#     second_string = 'empada'
#     print(is_anagram(first_string, second_string))
