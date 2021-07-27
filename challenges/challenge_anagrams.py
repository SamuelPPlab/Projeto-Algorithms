def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == "" or second_string == "" or len(first_string) != len(second_string):
        return False

    list_first_string = [char for char in first_string]
    list_second_string = [char for char in second_string]

    has_swapped = True
    num_of_iterations = 0
    while has_swapped:
        has_swapped = False

        for index in range(len(list_first_string) - num_of_iterations - 1):
            if list_first_string[index] > list_first_string[index + 1]:
                list_first_string[index], list_first_string[index + 1] = list_first_string[index + 1], list_first_string[index]
                has_swapped = True
        num_of_iterations += 1

    has_swapped = True
    num_of_iterations = 0
    while has_swapped:
        has_swapped = False

        for index in range(len(list_second_string) - num_of_iterations - 1):
            if list_second_string[index] > list_second_string[index + 1]:
                list_second_string[index], list_second_string[index + 1] = list_second_string[index + 1], list_second_string[index]
                has_swapped = True
        num_of_iterations += 1
    
    if list_first_string == list_second_string:
        return True
    
    return False

    


first_string = 'FERNANDO'
second_string = 'FERNANDA'
print(is_anagram(first_string, second_string))
