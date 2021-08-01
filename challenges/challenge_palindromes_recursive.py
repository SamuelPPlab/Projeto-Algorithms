def is_palindrome_recursive(word, low_index, high_index):
    word_list = list(word)
    if len(word) < 1:
        return False
    if low_index == high_index:
        return True
    if word_list[high_index] != word_list[low_index]:
        return False
    return is_palindrome_recursive(word_list, low_index + 1, high_index - 1)
