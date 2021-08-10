def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui """
    li = low_index
    hi = high_index
    try:
        if not word or word[li] != word[hi]:
            return False

        if len(word) < 3:
            return True

        return is_palindrome_recursive(word[1:-1], li, len(word[1:-1]) - 1)
    except TypeError:
        return False
