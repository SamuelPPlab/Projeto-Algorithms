def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word or (len(word) == 1) or (word == ''):
        return False
    if word[low_index] == word[high_index]:
        if low_index >= high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False

# 2 - python3 -m pytest tests/test_palindromes_recursive.py
