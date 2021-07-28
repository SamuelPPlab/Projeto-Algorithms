def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    print({'w': word, 'low': low_index, 'high': high_index})
    if word == "":
        return False
    elif len(word) == 1:
        return True
    elif word[low_index] != word[high_index]:
        return False
    new_word = word[1:high_index]
    print('neo', new_word)
    return is_palindrome_recursive(new_word, 0, len(new_word) - 1)


print(is_palindrome_recursive("", 0, len("AGUA") - 1))
