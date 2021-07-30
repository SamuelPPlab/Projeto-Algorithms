from typing import Counter


"""Although to run a serious benchmark the machine should run ONLY the program,
the execution times commented bellow may represent
a comparison of those algorithms"""


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


# 0.147181 ~  0.15807
def generate_counter_dict(lista):
    dic = {}

    for letra in lista:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1

    return dic


# 0.165924 ~ 0.168763 seconds
def recursive_dict(string, str_dict={}):
    if len(string) == 0:
        return str_dict
    str_dict[string[0]] = string.count(string[0])
    return recursive_dict(string.replace(string[0], ''), str_dict)


# 0.163752 ~ 0.184378
def slow_gen_counter_dict(lista):
    dic = {letra: 0 for letra in lista}

    for letra in lista:
        dic[letra] += 1

    return dic


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


# pivot for quicksort
def partition(array, low, high):
    # https://github.com/tryber/sd-07-project-algorithms/tree/luciano-berchon-project-algorithms
    i = low - 1
    pivot = array[high]

    for j in range(low, high):

        if array[j] <= pivot:

            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


# 2.41763 ~ 2.47492 seconds
def quicksort(array, low, high):
    # https://github.com/tryber/sd-07-project-algorithms/tree/luciano-berchon-project-algorithms
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)

    return array


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

    # Counter py method turned to be the fastest - I am not surprised at all
    # 0.076248 ~ 0.09043 seconds
    return Counter(first_string) == Counter(second_string)

    #  0.121676 ~ 0.122801 seconds
    # return remove_chars_list(first_string, second_string)

    # 0.133657 ~ 0.137959
    # return sorted(list(first_string)) == list(second_string).sort()

    # 0.147181 ~  0.15807
    """return generate_counter_dict(
        list(first_string)
    ) == generate_counter_dict(
        list(second_string)
    )"""

    # 0.174338 ~ 0.17686 seconds
    """return recursive_dict(
        second_string, {}
    ) == recursive_dict(
        first_string, {}
    )"""

    # 0.163752 ~ 0.184378
    """return slow_gen_counter_dict(
        list(first_string)
    ) == slow_gen_counter_dict(
        list(second_string)
    )"""

    #  0.21519 ~ 0.21801 seconds
    # return remove_chars(first_string, second_string)

    # 0.375300 ~ 0.386072 seconds
    # return slow_dict(first_string, second_string)

    #  2.41763 ~ 2.47492 seconds
    # return quicksort(
    #      list(first_string), 0, len(first_string) - 1
    #  ) == quicksort(
    #      list(second_string), 0, len(second_string) - 1
    #  )

    # 5.7930 ~ 5.82011 seconds
    # return selection_sort(first_string) == selection_sort(second_string)
