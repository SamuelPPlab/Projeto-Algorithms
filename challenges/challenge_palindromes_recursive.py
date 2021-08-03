def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index == high_index:
        return True
    if word[high_index] == word[low_index]:
        return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))
    return False
