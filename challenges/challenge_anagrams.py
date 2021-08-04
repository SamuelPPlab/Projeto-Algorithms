def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    str01 = list(first_string.lower())
    str02 = list(second_string.lower())
    if len(str01) != len(str02):
        return False
    if ((str01 or str02 == '') or (str01 or str02 != str)):
        return False

    return False

# 3 - python3 -m pytest tests/test_anagrams.py
