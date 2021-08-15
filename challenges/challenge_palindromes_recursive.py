def reverse(list):
    if len(list) < 2:
        return list
    else:
        reversed = reverse(list[1:])
        return reversed + list[0]


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    return word == reverse(word)
