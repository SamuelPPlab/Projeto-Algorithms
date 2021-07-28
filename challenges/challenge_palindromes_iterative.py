def is_palindrome_iterative(word):
    if not word:
        return False
    valida = [
        item
        for item in range(len(word) // 2)
        if not word[item] != word[len(word) - 1 - item]
    ]
    for item in range(len(word) // 2):
        if word[item] != word[len(word) - 1 - item]:
            return False
    return valida
