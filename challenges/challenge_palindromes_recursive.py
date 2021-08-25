def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    print(low_index)
    if len(word) == 1 or low_index == high_index:
        return True
    if word == '' or word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index +1, high_index -1)
