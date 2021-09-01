def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) <= 1:
        return word[low_index] == word[high_index]
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word[1:-1], low_index, high_index - 2)
    return False
