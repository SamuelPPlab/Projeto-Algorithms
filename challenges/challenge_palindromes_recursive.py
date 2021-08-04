def is_palindrome_recursive(word, low, high):
    if word == '' or word[low] != word[high]:
        return False
    if len(word) == 1:
        return True
    return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]) - 1)
