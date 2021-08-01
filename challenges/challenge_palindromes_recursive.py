from helpers.Number import ONE, ZERO, MINUS_ONE


def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if len(word) == ONE:
        return True

    if word[ZERO] != word[MINUS_ONE]:
        return False

    return is_palindrome_recursive(
        word[(low_index + 1):(low_index - 1)],
        low_index,
        high_index
    )
