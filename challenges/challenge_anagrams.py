def is_anagram(first_string, second_string):
    if not first_string:
        return False
    if not second_string:
        return False
    first_word = list(first_string)
    second_word = list(second_string)
    if (len(first_word) != len(second_word)):
        return False

    if quicksort(first_word, 0, len(first_word) - 1) == quicksort(
        second_word, 0, len(second_word) - 1
    ):
        return True
    else:
        return False


def insertion_sort(array):
    for i in range(len(array)):
        value = array[i]
        position = i

        while position > 0 and array[position - 1] > value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = value
    return array


def bubble_sort(array):
    # variável utilizado na iteração
    # para marcar se houve ou não trocas naquela iteração
    # Quando falsa, indica que o array está ordenado
    swapped = True

    # armazena o número de iterações para evitar
    # a iteração sobre índices já ordenados
    iterations = 0

    # Enquanto ainda não está ordenado (ocorreram trocas na iteração)
    while swapped:
        swapped = False

        # percorra o array até o ultimo índice não ordenado
        for i in range(len(array) - iterations - 1):
            # caso a posição corrente seja maior que a posterior
            if array[i] > array[i + 1]:
                # realiza a troca entre as posições
                array[i], array[i + 1] = array[i + 1], array[i]
                # marca que tivemos trocas nesta iteração
                swapped = True
        iterations += 1
    return array


def quicksort(array, low, high):
    # caso base: se já atingiu a menor porção (1)
    if len(array) == 1:
        # retorne o array
        return array

    # os índices irão se cruzar quando o array estiver ordenado
    if low < high:
        # índice da partição é o índice onde o array foi divido
        # e é determinado a partir do pivô.
        # Este índice já está ordenado
        partition_index = partition(array, low, high)

        # Ordena os elementos presentes antes da partição (menores que o pivô)
        # e depois (maiores que o pivô)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados
def partition(array, low, high):
    # índice do menor elemento
    i = low - 1
    # o pivô será escolhido
    # através do índice que divide o array
    pivot = array[high]  # pivot

    # itera sobre os elementos
    for j in range(low, high):

        # se o elemento corrente é menor ou igual ao pivô
        if array[j] <= pivot:

            # incrementa o índice do menor elemento
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
