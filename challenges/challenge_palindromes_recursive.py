def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or word[low_index] != word[high_index]:
        return False

    while low_index < high_index:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True

# src: https://medium.com/guvi/recursive-python-program-to-test-if-a-string-is-
# a-palindrome-or-not
# -1eb69f2222ec
