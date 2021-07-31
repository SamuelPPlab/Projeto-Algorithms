def is_anagram(first_string, second_string):
    list1 = list_sort(list(first_string))
    list2 = list_sort(list(second_string))

    if list1 == list2:
        return True
    return False


def list_sort(inlist):
    # ordenação lista @luc-zago
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = list_sort([x for x in inlist[1:] if x < pivot])
        greater = list_sort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
