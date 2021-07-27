def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    return word == reverse(word)


def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + list[0]

