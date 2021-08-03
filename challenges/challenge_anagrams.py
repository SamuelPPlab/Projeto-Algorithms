def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_string = list(first_string.lower())
    second_string = list(second_string.lower())
    str01 = sorted(first_string)
    str02 = sorted(second_string)
    # if(len(str01) != len(str02) or (str01 or str02 == '') or (str01 or str02 != str)):
    #     return False
    if sorted(str01) == sorted(str02):
        return True
    return False
# 3 - python3 -m pytest tests/challenge_palindromes_recursive.py
