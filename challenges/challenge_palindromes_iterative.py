def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    changed_word = word[::-1]
    return word == changed_word
