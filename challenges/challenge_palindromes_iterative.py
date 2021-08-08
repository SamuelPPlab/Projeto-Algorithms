def is_palindrome_iterative(word):
    reversed_word = word[::-1]
    index = 0

    if not word:
        return False

    for char in word:

        if char != reversed_word[index]:
            return False

        index += 1

    return True
