def is_palindrome_iterative(word):
    if not word:
        return False
    inverted_word = word[::-1]
    return word == inverted_word
