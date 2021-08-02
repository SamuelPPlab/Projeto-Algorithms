def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    list1 = list(first_string)
    list2 = list(second_string)

    for letra in list1:
        for letra2 in list2:
            if letra2 == letra:
                list1.remove(letra)
                list2.remove(letra2)

    if len(list1) == 0 and len(list2) == 0:
        return True
    else:
        return False


is_anagram("perda", "pedra")