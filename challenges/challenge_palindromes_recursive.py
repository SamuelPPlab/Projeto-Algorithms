def is_palindrome_recursive(word, low_index, high_index):
    if word == "" or word[low_index] != word[high_index]:
        return False
    elif low_index == high_index:
        return True
    new_Hindex = high_index - 1
    new_Lindex = low_index + 1
    return is_palindrome_recursive(word, new_Lindex, new_Hindex)
