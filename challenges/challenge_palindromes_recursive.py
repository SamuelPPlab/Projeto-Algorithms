def is_palindrome_recursive(word, low_index, high_index):
    # if len(word) < 2:
    #     return True
    # elif word[0] != word[-1]:
    #     return False
    # else:
    #     return is_palindrome_recursive(word[1:-1], low_index, high_index)
    try:
        if low_index == high_index:
            return True
        elif word[low_index] != word[high_index]:
            return False
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False


if __name__ == "__main__":
    word = "ANA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    # saída: True

    word = "SOCOS"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    # saída: True

    word = "REVIVER"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    # saída: True

    word = "COXINHA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    # saída: False

    word = "AGUA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    # saída: False
