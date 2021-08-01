def is_anagram(first_string, second_string):
    return bubble_sort(first_string) == bubble_sort(second_string)

# REF: https://app.betrybe.com/course/computer-science/algoritmos-e-estrutura-de-dados/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/32a9d9fa-341d-4bdb-af65-eedc37a6082e/algoritmos-de-ordenacao/28628db5-3bd5-4561-aa1d-53b51818494f?use_case=side_bar
def bubble_sort(array):
    array = list(array)
    # variável utilizado na iteração
    # para marcar se houve ou não trocas naquela iteração
    # Quando falsa, indica que o array está ordenado
    has_swapped = True

    # armazena o número de iterações para evitar
    # a iteração sobre índices já ordenados
    num_of_iterations = 0

    # Enquanto ainda não está ordenado (ocorreram trocas na iteração)
    while has_swapped:
        has_swapped = False

        # percorra o array até o ultimo índice não ordenado
        for i in range(len(array) - num_of_iterations - 1):
            # caso a posição corrente seja maior que a posterior
            if array[i] > array[i + 1]:
                # realiza a troca entre as posições
                array[i], array[i + 1] = array[i + 1], array[i]
                # marca que tivemos trocas nesta iteração
                has_swapped = True
        num_of_iterations += 1
    array = ''.join(array)
    return array
