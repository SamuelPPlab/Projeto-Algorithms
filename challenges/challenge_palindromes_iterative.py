def is_palindrome_iterative(word):
    if word == '':
        return False
    for idx in range(len(word) // 2):
        if word[idx] != word[-1 - idx]:
            return False
    return True
