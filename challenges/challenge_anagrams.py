def merge(left, rigth):
    result = []
    while left != [] and rigth != []:
        if left[0] <= rigth[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(rigth[0])
            rigth = rigth[1:]
    while left != []:
        result.append(left[0])
        left = left[1:]

    while rigth != []:
        result.append(rigth[0])
        rigth = rigth[1:]
    return result


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    left = []
    rigth = []
    metade = (len(lista)/2)
    for i in range(len(lista)):
        if i < metade:
            left.append(lista[i])
        else:
            rigth.append(lista[i])
    # print('left antes da recursividade', left)
    # print('rigth antes da recursividade', rigth)
    left = merge_sort(left)
    rigth = merge_sort(rigth)
    return merge(left, rigth)


def is_anagram(first_string, second_string):
    if (first_string == '') or (second_string == ''):
        return False
    first = merge_sort(first_string)
    second = merge_sort(second_string)
    pos = 0
    iguais = True

    while pos < len(first_string) and iguais:
        if first[pos] == second[pos]:
            pos = pos + 1
        else:
            iguais = False
    return iguais
