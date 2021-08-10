def is_palindrome_iterative(word):
    if not word:
        return False

    reversed = word[::-1]
    return reversed == word
