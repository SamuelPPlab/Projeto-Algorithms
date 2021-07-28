def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif len(word) < 2:
        return True
    else:
        word[low_index] == word[high_index]
        return is_palindrome_recursive(
            word[1:-1], low_index, len(word[1:-1]) - 1
        )
