def is_palindrome_recursive(word, low, high):
    if word == "" or word[low] != word[high]:
        return False
    if low == high:
        return True

    high_index = high - 1
    low_index = low + 1
    return is_palindrome_recursive(word, low_index, high_index)
