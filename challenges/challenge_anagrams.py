def is_anagram(first_string, second_string):
    if(qsort(list(first_string)) == qsort(list(second_string))):
        return True
    else:
        return False


def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
