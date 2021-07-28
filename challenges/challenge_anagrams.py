def is_anagram(first_string, second_string):
    first_list = [letter for letter in first_string]
    second_list = [letter for letter in second_string]

    for index, letter in enumerate(first_list):
        letter_index = None

        for current_index in range(index, len(second_list)):
            if letter == second_list[current_index]:
                letter_index = second_list[current_index]
                break

        if not letter_index:
            break

        second_list[index], second_list[current_index] = (
            second_list[current_index],
            second_list[index],
        )

    return first_list == second_list
