# stackOverflow
# https://stackoverflow.com/questions/3855537/fastest-way-to-sort-in-python

def quick_sort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = quick_sort([x for x in inlist[1:] if x < pivot])
        greater = quick_sort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


def is_anagram(first_string, second_string):
    first_string_ordered = ''.join(quick_sort(list(first_string)))
    second_string_ordered = ''.join(quick_sort(list(second_string)))

    if first_string_ordered == second_string_ordered:
        return True

    return False
