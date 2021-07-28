def is_palindrome_iterative(word):
    if not word:
        return False
    else:
        word == word[::-1]
        return True
