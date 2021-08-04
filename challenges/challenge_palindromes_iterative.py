def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == "":
        return False
    if word == word[::-1]:
        return True

# 5 - python3 -m pytest tests/test_palindromes_iterative.py
