def bubble_sort(string):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(string) - num_of_iterations - 1):
            if string[i] > string[i + 1]:
                string[i], string[i + 1] = string[i + 1], string[i]
                has_swapped = True
        num_of_iterations += 1
    return string


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    ordered_first_string = bubble_sort(list(first_string))
    ordered_second_string = bubble_sort(list(second_string))

    if ordered_first_string == ordered_second_string:
        return True
    else:
        return False
