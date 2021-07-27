def is_palindrome_recursive(word, low_index, high_index):
    if (len(word) == 0):
        return False
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return is_palindrome_recursive(word[1:-1], 0, len(word) - 1)
