def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == '':
        return False
    low = low_index or 0
    high = high_index or len(word) - 1
    if word[low] != word[high]:
        return False
    if low == len(word) - 1:
        return True
    return is_palindrome_recursive(word, low + 1, high - 1)
