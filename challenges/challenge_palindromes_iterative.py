def is_palindrome_iterative(word):
    if word == '' or word != word[::-1]:
        return False
    else:
        return True

# teste do avaliador
