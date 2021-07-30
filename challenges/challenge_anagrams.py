from typing import Counter


#  0.121676 ~ 0.122801 seconds
def remove_chars_list(first_string, second_string):
    # https://github.com/tryber/sd-07-project-algorithms/tree/MoisesSantana-Algorithms
    first_list = list(first_string)
    second_list = list(second_string)
    for letter in first_list:
        try:
            index = second_list.index(letter)
        except ValueError:
            return False

        second_list.remove(second_list[index])

    return True


# 0.174338 ~ 0.17686 seconds
def optimized_dict(string, str_dict = {}):
    if len(string) == 0:
        return str_dict
    if string[0] in str_dict:
        return optimized_dict(string[1:], str_dict)
    str_dict[string[0]] = string.count(string[0])
    return optimized_dict(string.replace(string[0], ''), str_dict)


#  0.21519 ~ 0.21801 seconds
def remove_chars(first_string, second_string):
    for letter in first_string:
        try:
            index = second_string.index(letter)
        except ValueError:
            return False

        second_string = second_string[:index] + second_string[index + 1:]

    return True

# 0.375300 ~ 0.386072 seconds
def slow_dict(f_str, s_str):
    first_dict = {i: f_str.count(i) for i in f_str}
    second_dict = {a: s_str.count(a) for a in s_str}
    return first_dict == second_dict


# 5.7930 ~ 5.82011 seconds
def selection_sort(string):
    str_list = list(string)
    for i in range(len(str_list)):
        min_index = i
        for j in range(i + 1, len(str_list)):
            if str_list[min_index] > str_list[j]:
                min_index = j
        str_list[i], str_list[min_index] = str_list[min_index], str_list[i]
    return str_list



def is_anagram(first_string, second_string):
    if (
        not isinstance(first_string, str)
        or not isinstance(second_string, str)
        or len(first_string) != len(second_string)
    ):
        return False

    # after some tests the python method turned to be the fastest - I am not surprised at all
    # 0.076248 ~ 0.09043 seconds
    return Counter(first_string) == Counter(second_string)

    #  0.121676 ~ 0.122801 seconds
    # return remove_chars_list(first_string, second_string)

    # 0.174338 ~ 0.17686 seconds
    # return optimized_dict(second_string, {}) == optimized_dict(first_string, {})

    #  0.21519 ~ 0.21801 seconds
    # return remove_chars(first_string, second_string)

    # 0.375300 ~ 0.386072 seconds
    # return slow_dict(first_string, second_string)
    
    # 5.7930 ~ 5.82011 seconds
    # return selection_sort(first_string) == selection_sort(second_string)
