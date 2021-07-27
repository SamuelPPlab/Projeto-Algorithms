def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) < 2:
        return True
    elif word[low_index] == word[high_index]:
        return True and is_palindrome_recursive(
            word[1:-1], 0, len(word[1:-1]) - 1
        )
    else:
        return False
