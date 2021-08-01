from helpers.Number import MINUS_ONE


def is_palindrome_iterative(word):
    if word == "":
        return False

    return word == word[::MINUS_ONE]
