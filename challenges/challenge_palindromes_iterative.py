def is_palindrome_iterative(word):
    if word and word == word[::-1]:
        return True
    return False
