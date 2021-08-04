def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "" or word[low_index] != word[high_index]:
        return False
    if len(word) < 2:
        return True
    return is_palindrome_recursive(word[1:-1], low_index, len(word[1:-1]) - 1)
