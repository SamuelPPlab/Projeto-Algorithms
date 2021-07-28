# FONTE: https://algoritmosempython.com.br/cursos
# /algoritmos-python/pesquisa-ordenacao/quicksort/


def QuickSort(word):
    if len(word) == 0:
        return word
    pivot = word[0]
    front = QuickSort([smaller for smaller in word[1:] if smaller <= pivot])
    behind = QuickSort([larger for larger in word[1:] if larger > pivot])
    return front + [pivot] + behind


def is_anagram(first_string, second_string):
    order_first_string = ''.join(QuickSort(list(first_string)))
    order_second_string = ''.join(QuickSort(list(second_string)))
    return order_first_string == order_second_string


# if __name__ == '__main__':
#     # saída: True
#     # saída: True
#     # saída: True
#     # saída: False

#     first_string = "amor"
#     second_string = "roma"
#     result = is_anagram(first_string, second_string)
#     print(result)
#     # Explicação: Nesse caso o retorno da função é True, pois a palavra "roma" é um anagrama de "amor".

#     first_string = "pedra"
#     second_string = "perda"
#     result = is_anagram(first_string, second_string)
#     print(result)
#     # Explicação: Nesse caso o retorno também é True. Na palavra "pedra", trocamos o "d" de lugar com o "r" e formamos "perda", sendo assim um anagrama.

#     first_string = "pato"
#     second_string = "tapo"
#     result = is_anagram(first_string, second_string)
#     print(result)

#     # Agora vamos pra um exemplo onde não existe um anagrama
#     first_string = "coxinha"
#     second_string = "empada"
#     result = is_anagram(first_string, second_string)
#     print(result)
