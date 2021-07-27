def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    word_reverse = ""
    cont = len(word) - 1
    for letter in word:
        word_reverse += word[cont]
        cont -= 1
    if word == word_reverse:
        return True
    return False
