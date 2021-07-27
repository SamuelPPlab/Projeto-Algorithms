def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    status = True
    if len(word) > 1:
        if word[0] == word[high_index]:
            new_word = word[low_index + 1: high_index]
            status = is_palindrome_recursive(
                new_word, low_index, len(new_word) - 1
            )
        else:
            return False
    return status
