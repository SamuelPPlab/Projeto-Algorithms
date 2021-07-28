def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif word[0] != word[-1]:
        return False
    else:
        len(word) < 2
        return is_palindrome_recursive(word[1:-1])