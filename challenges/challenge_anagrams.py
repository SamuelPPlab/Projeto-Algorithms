def is_anagram(first_string, second_string):
    length = len(first_string) != len(second_string)
    if not first_string or not second_string or length:
        return False
    first_sorted_list = merge_sort(list(first_string))
    second_sorted_list = merge_sort(list(second_string))
    if first_sorted_list != second_sorted_list:
        return False

    return True


def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    mid_point = len(list_to_sort) // 2
    left_partition = merge_sort(list_to_sort[:mid_point])
    right_partition = merge_sort(list_to_sort[mid_point:])
    sorted_list = merge(left_partition, right_partition)
    return sorted_list


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

# https://towardsdatascience.com/how-to-implement-merge-sort-algorithm-in-python-4662a89ae48c
