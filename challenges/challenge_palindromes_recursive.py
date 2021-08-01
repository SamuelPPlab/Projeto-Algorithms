def is_palindrome_recursive(word, low_index, high_index):
    if word == "" or word[low_index] != word[high_index]:
        return False
    word = word[1:high_index]
    if len(word) == 1 or word == "":
        return True
    return is_palindrome_recursive(word, 0, len(word) - 1)

