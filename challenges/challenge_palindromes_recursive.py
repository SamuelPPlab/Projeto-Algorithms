def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word is None or word == "":
        return False
    if low_index > high_index:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False


# word = "AGUA"
# print(is_palindrome_recursive(word, 0, len(word) - 1))
