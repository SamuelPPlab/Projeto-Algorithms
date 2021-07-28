def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) < 2:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]) - 1)

# referencia
# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
