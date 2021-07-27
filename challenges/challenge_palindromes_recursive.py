def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if high_index == 0:
        return True
    else:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word[1:-1], 0, high_index-2)
        return False


# if __name__ == '__main__':
#     # saída: True
#     # saída: True
#     # saída: True
#     # saída: False
#     # saída: False
#     word = "ANA"
#     is_palindrome = is_palindrome_recursive(word, 0, len(word)-1)
#     print(f'Saida esperada True recebida {is_palindrome}')

#     word = "SOCOS"
#     is_palindrome = is_palindrome_recursive(word, 0, len(word)-1)
#     print(f'Saida esperada True recebida {is_palindrome}')

#     word = "REVIVER"
#     is_palindrome = is_palindrome_recursive(word, 0, len(word)-1)
#     print(f'Saida esperada True recebida {is_palindrome}')

#     word = "COXINHA"
#     is_palindrome = is_palindrome_recursive(word, 0, len(word)-1)
#     print(f'Saida esperada True recebida {is_palindrome}')

#     word = "AGUA"
#     is_palindrome = is_palindrome_recursive(word, 0, len(word)-1)
#     print(f'Saida esperada True recebida {is_palindrome}')
