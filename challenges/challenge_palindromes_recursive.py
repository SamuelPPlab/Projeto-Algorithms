def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    return (word[low_index] == word[high_index] and
            (low_index > high_index or
             is_palindrome_recursive(word, low_index + 1, high_index - 1)))
