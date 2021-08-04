def is_palindrome_recursive(word, low, high):
    if not word or word[low] != word[high]:
        return False

    if len(word) < 3:
        return True

    return is_palindrome_recursive(word[1:-1], low, len(word[1:-1]) - 1)
