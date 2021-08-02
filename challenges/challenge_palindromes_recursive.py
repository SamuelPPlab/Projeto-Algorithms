def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word[low_index:high_index], 0, -1)

# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
