def is_palindrome_iterative(word):
    if not word:
        return False
    status = True
    for index in range(len(word) // 2):
        if word[index] != word[len(word) - 1 - index]:
            status = False

    return status
