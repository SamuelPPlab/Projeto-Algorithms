def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if ((first_string == '') or (second_string == '')):
        return False

    for index in range(len(first_string)):

        if(second_string.count(first_string[index]) !=
           first_string.count(first_string[index])):
            return False
    return True
