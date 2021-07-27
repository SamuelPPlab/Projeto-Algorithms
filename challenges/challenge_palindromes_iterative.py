def is_palindrome_iterative(word):
    if word == "":
        return False
    return word == word[::-1]

# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/