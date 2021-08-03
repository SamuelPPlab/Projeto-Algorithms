def is_anagram(first_string, second_string):
    if not first_string or not second_string or len(first_string) != len(second_string):
        return False
    else:
       first_string = list(first_string.lower())
       second_string = list(second_string.lower())
       for letra in first_string:
            if letra not in second_string:
               return False
            second_string.remove(letra)
    return True

    # https://stackoverflow.com/questions/58396590/the-most-efficient-way-testing-2-strings-for-anagrams-python