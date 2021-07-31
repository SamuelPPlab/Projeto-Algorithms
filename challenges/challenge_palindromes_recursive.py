def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1], 0, 0)
