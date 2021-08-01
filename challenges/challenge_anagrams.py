# From google search "quick sort python"
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    return quick_sort_recursion(array, begin, end)
################


def _sort(str):
    str_list = list(str)
    quick_sort(str_list)
    return str_list


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    return _sort(first_string) == _sort(second_string)
