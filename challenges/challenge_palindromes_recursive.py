def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not word:
        return False
    elif len(word) <= 1:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word[1:-1], 0, len(word[1:-1]) - 1)
    else:
        return False


# if __name__ == "__main__":
#     word = "SSNSS"
#     print(is_palindrome_recursive(word, 0, len(word) - 1))
