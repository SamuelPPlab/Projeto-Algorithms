def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    left, right = 0, len(word) - 1

    while left < len(word) // 2:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True
