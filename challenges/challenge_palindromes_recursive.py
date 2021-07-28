def is_palindrome_recursive(word, low_index, high_index):
    # https://www.youtube.com/watch?v=92UyahoAne4
    if len(word) < 1:
        return False
    if len(word) == 1:
        return True
    else:
        print(word[(len(word) - 1)])
        print(word[-1])
        return word[low_index] == word[-1] and is_palindrome_recursive(
            word[1:-1], low_index, (len(word) - 1)
        )
