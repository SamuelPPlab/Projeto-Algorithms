def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    first_word = break_word(first_string)
    second_word = break_word(second_string)
    insertion_sort(first_word)
    insertion_sort(second_word)
    if first_word == second_word:
        return True
    return False


def break_word(word):
    empty_array = []
    for letter in word:
        empty_array.append(letter)
    return empty_array


# exemplo Bloco 36 - Algoritmos e Estrutura de Dados - course
def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            # move as posições para a direita
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        # colocamos o elemento em sua nova posição
        array[current_position] = current_value
    return array
