def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    try:
        if word == "":
            return False
        return word == word[::-1]
    except TypeError:
        return False
