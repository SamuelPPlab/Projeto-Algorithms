def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    return is_palindrome_recursive(
        word[low_index:high_index], low_index, high_index
    )

