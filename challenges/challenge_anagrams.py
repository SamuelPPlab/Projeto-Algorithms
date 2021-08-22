def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

def is_anagram(first_string, second_string):

    return quicksort(first_string) == quicksort(second_string)


# https://www.delftstack.com/pt/howto/python/sort-list-alphabetically/