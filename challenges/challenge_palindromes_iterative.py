def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False

    reversed_word = word[::-1]
    return reversed_word == word

# referencia carlos8v pull #58
