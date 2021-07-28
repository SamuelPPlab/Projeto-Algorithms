def is_palindrome_recursive(word, low, high):
        if not word:
            return False

        if word[low] != word[high]:
            return False

        if low == high or low == high + 1:
            return True

        else:
            return is_palindrome_recursive(word, low + 1, high - 1)