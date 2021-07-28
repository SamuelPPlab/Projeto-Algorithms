def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 2:
        return bool(word)

    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word[1:-1], 0, -1)

    return False
