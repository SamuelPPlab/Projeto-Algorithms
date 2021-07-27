def check_is_palindrome(word, low_index, high_index):
    if low_index == high_index:
        return word[high_index]

    return word[high_index] + check_is_palindrome(
        word, low_index, high_index - 1
    )


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "":
        return False

    palindrome = check_is_palindrome(word, low_index, high_index)

    if word == palindrome:
        return True

    return False


# word = ""
# print(is_palindrome_recursive(word, 0, len(word) - 1))
