def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if low_index == high_index:
            return True
        elif word[high_index] != word[low_index]:
            return False
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False
