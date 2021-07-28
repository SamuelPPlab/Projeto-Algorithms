def is_palindrome_iterative(word):
    if len(word) < 1:
        return False
    palindrome = list(word)
    palindrome.reverse()
    palindrome = ''.join(palindrome)
    return palindrome == word
