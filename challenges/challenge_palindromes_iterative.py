def is_palindrome_iterative(word):
    if not word:
        return False
    status = True
    midlle = len(word) // 2
    for index in range(len(word)):
        if index == midlle:
            break
        if word[index] != word[len(word) - 1 - index]:
            status = False

    return status
