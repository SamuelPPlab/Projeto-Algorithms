def is_palindrome_iterative(word):
    if not str(word) or len(word) <= 0:
        return False
    return word == word[::-1]