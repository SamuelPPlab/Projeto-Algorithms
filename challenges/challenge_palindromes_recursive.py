def is_palindrome_recursive(word, low_index, high_index):
    word_list = list(word)
    if ((low_index - high_index)< 2):
        return True
    if (word_list[high_index] != word_list[low_index]):
        return False
    return is_palindrome_recursive(word_list, low_index, high_index ]
