def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    first = list(first_string)
    second = list(second_string)

    first_str_sorted = sort_func(first)
    second_str_sorted = sort_func(second)

    for i in range(len(first_string)):
        if first_str_sorted[i] != second_str_sorted[i]:
            return False
    return True


def sort_func(string):  # https://www.youtube.com/watch?v=kFeXwkgnQ9U&t=1s
    length = len(string)
    if length <= 1:
        return string
    else:
        pivot = string.pop()
    letter_after = []
    letter_before = []

    for letter in string:
        if letter > pivot:
            letter_after.append(letter)
        else:
            letter_before.append(letter)

    return sort_func(letter_before) + [pivot] + sort_func(letter_after)
