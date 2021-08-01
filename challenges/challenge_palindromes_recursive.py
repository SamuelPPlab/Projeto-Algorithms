def is_palindrome_recursive(word, low_index, high_index):
    if (
        len(word) < 1
        or word is None
    ):
        return False
    if (
        len(word) <= 2
        and word[0] == word[len(word) - 1]
    ):
        return True
    if (word[0] == word[len(word) - 1]):
        return is_palindrome_recursive(
            word[1: len(word) - 1], low_index, high_index - 1)
    else:

        return False
