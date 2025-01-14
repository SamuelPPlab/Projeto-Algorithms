def sorting_algorithm(word):
    # código baseado no dia 36.3 do course
    # https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-
    # 44ea-488d-a74d-216b1ac79b04/conteudos/
    # 118f97fe-3cc2-4468-a14c-ca8c341cadc2/algoritmos-de-ordenacao/a3ba0c1f-1835-4956-ba4a-42f376d3d555?use_case=side_bar
    array = list(word)
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]

    return array


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    sorted_first_string = sorting_algorithm(first_string)
    sorted_second_string = sorting_algorithm(second_string)
    if sorted_first_string == sorted_second_string:
        return True
    else:
        return False
