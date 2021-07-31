def is_palindrome_recursive(word, low_index=0, high_index=0):
    if len(word) == 0:
        return False
    next_word = word[1:-1]
    if word[0] == word[-1]:
        if len(next_word) <= 1:
            return True
        else:
            return is_palindrome_recursive(next_word)
    return False
