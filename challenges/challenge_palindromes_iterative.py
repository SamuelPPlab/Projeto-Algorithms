def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    i = 0
    if word == '':
        return False
    

    while i < len(word) // 2:
        if word[i] != word[len(word) - i - 1]:
            return False
        i += 1
    return True


print(is_palindrome_iterative('amatama'))
