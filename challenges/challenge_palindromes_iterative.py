def is_palindrome_iterative(word):
    if not word:
        return False
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
