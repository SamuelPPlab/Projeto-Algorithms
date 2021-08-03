def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if low_index <= high_index:
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
            return is_palindrome_recursive(word, low_index, high_index)
        else:
            return False
    return True


# if __name__ == "__main__":
#    word = "SOCOS"
#    print(is_palindrome_recursive(word, 0, len(word) - 1))
