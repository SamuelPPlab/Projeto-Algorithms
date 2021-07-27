def is_palindrome_recursive(word, low_index, high_index):
    if (not word) or (word[low_index] != word[high_index]):
        return False

    if high_index == 1:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


'''
    [a]rar[a] - 0 - 4
    a[r]a[r]a - 1 - 3
    ar[[a]]ra - 2 - 2
    arara - 3 - 1 (True - linha 4)

    [m]aç[ã] - 0 - 3 (False - linha 2)

    [a]bbacb[a] - 0 - 6
    a[b]bac[b]a - 1 - 5
    ab[b]a[c]ba - 2 - 4 (False - linha 2)
'''
