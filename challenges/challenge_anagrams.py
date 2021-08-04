from collections import Counter


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    return Counter(first_string) == Counter(second_string)


# https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe#:~:text=The%20pythonic%20way,s1)%20%3D%3D%20Counter(s2)