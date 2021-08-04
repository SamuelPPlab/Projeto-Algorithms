def is_anagram(first_string, second_string):
    if (first_string == ""
            or second_string == ""
            or len(first_string) != len(second_string)):

        return False

    counter = 0
    second_string_array = list(second_string)
    for i in range(len(first_string)):
        for j in range(len(second_string_array)):
            if first_string[i] == second_string_array[j]:
                second_string_array.remove(second_string_array[j])
                counter += 1
                break
    return counter == len(first_string)
