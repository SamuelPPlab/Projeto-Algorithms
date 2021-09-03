def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False

    if high_index - low_index in [0, 1]:
        if word[low_index] == word[high_index]:
            return True
        else:
            return False
    else:
        if word[low_index] == word[high_index]:
            palindrome = True
        else:
            palindrome = False
        return palindrome and is_palindrome_recursive(word,
                                                      low_index + 1,
                                                      high_index - 1)
