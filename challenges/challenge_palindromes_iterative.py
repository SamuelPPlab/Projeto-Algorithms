def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    i = 0
    if word == '':
        return False
    result = True
    while i < len(word) // 2 + 1:
        if word[i] != word[len(word)-i-1]:
            result = False
        i += 1
    return result
