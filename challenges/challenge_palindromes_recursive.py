def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index == high_index:
        # Se o length do low_index e high_index for o mesmo, significa que
        # não precisamos mais realizar comparações pois chegamos na ultima
        # letra.
        return True

    if word[low_index] != word[high_index]:
        # comparamos se as letras na posição do low_index e do high_index
        # são diferentes. Caso sejam é retornado False, pois não é um
        # palindromo.
        return False

    if low_index < high_index:
        # Somamos 1 no low_index e subtraimos 1 no high_index exatamente para
        # comparar os caracteres de suas respectivas posições
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True


# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
