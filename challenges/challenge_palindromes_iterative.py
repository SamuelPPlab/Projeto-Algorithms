def is_palindrome_iterative(word):
    if word == "":
        return False
    reverse = word[::-1]
    if reverse == word:
        return True
    return False


# if __name__ == "__main__":
#    word = "SOCOS"
#    print(is_palindrome_iterative(word))
