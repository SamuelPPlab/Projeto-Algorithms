def is_anagram(first_string, second_string):

    first_string_list = [letter for letter in first_string]
    second_string_list = [letter for letter in second_string]

    for index, letter in enumerate(first_string_list):
        letter_index = None

        for current_index in range(index, len(second_string_list)):
            if letter == second_string_list[current_index]:
                letter_index = second_string_list[current_index]
                break

        if not letter_index:
            break

        second_string_list[index], second_string_list[current_index] = (
            second_string_list[current_index],
            second_string_list[index],
        )

    return first_string_list == second_string_list
