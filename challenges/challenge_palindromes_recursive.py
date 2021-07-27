def is_palindrome_recursive(word, low, high):
    if not word:
        return False
    middle = (low + high) // 2
    if (low > middle):
        return True
    if (word[low] == word[high]):
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False

# Verifiquei que a primeira e a ultima letra devem ser iguais, assim como a
# segunda e a penúltima. Se em algum momento isso não acontecer, retorna falso
# Caso contrário, quando chega no meio da palavra não precisa verificar mais e
# retorna True


# word = "ABAABA"
# print(is_palindrome_recursive(word, 0, len(word) - 1))
