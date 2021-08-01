def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    '''low_index é a primeira letra, high_index é a última letra'''
    if word[low_index] != word[high_index]:
        return False
    elif low_index == high_index:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
# entendi que vai comparar letra por letra, de fora para dentro
