def is_palindrome_iterative(word):
    """ Testa se uma string é palíndromo usando iteração. """
    if len(word) == 0:
        return False
    return word == word[::-1]
