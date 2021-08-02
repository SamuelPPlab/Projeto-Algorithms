def is_palindrome_iterative(word):
    if len(word) == 1:
        return True
    if not word:
        return False
    if word == ''.join(list(word)[::-1]):
        return True
    else:
        return False
