def is_palindrome_iterative(word):
    if not word:
        return False
    reversed = ""
    for index in range(1, len(word) + 1):
        reversed = reversed + word[len(word) - index]
    return word == reversed
