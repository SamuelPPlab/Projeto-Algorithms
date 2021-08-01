def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    elif low_index == high_index:
        if list(word)[low_index] == list(word)[high_index]:
            return True
    elif list(word)[low_index] == list(word)[high_index]:
        if low_index + 1 == high_index:
            return True
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else: 
        return False

print(is_palindrome_recursive("socos", 0, 4))
