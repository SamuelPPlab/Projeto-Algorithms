def is_palindrome_recursive(word, low_index, high_index):
    letters = list(word)
    if not str(word) or len(word) <= 0:
        return False
    if letters[high_index] != letters[low_index]:
        return False
    if low_index == high_index:
        return True
    return is_palindrome_recursive(letters, low_index + 1, high_index - 1)
