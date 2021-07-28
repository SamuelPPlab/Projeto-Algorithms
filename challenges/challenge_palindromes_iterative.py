def is_palindrome_iterative(word):
    if not word:
        return False
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    return False


if __name__ == "__main__":
    word = ""
    print(is_palindrome_iterative(word))
    # saída: True

    word = "SOCOS"
    print(is_palindrome_iterative(word))
    # saída: True

    word = "REVIVER"
    print(is_palindrome_iterative(word))
    # saída: True

    word = "COXINHA"
    print(is_palindrome_iterative(word))
    # saída: False

    word = "AGUA"
    print(is_palindrome_iterative(word))
    # saída: False
