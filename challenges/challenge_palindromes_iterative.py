def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    word_salad = list(word)
    reversed_order = []
    for item in word_salad:
        reversed_order.insert(0, item)
    if word == '' or word_salad != reversed_order:
        return False
    return True

