def is_palindrome_iterative(word):
    if not word:
        return False

    reversed_word = word[::-1]
    return reversed_word == word
