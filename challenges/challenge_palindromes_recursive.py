def is_palindrome_recursive(word, low, high):
    if not word or word[low] != word[high]:
        return False

    if len(word) == 3:
        return True

    new_word = word[1:-1]

    return is_palindrome_recursive(new_word, low, len(new_word) - 1)
