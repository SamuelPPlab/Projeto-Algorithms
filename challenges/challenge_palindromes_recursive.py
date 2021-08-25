def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    print(word)
    if len(word) == 1:
        return word
    else:
        return f'{word[-1]}' + is_palindrome_recursive(word[:-1], 0, 0)
        
print(is_palindrome_recursive('batuta', 3, 2))