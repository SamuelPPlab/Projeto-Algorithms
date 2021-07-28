def is_anagram(first_string, second_string):
    str1_list = list(first_string)
    quicksort(str1_list)
    str2_list = list(second_string)
    quicksort(str2_list)

    if str1_list != str2_list:
        return False
    return True


# https://www.youtube.com/watch?v=wx5juM9bbFo video sobre o quicksort
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


# if __name__ == "__main__":
#     str1_list = "pedra"
#     str2_list = "perda"
# print(is_anagram(str1_list, str2_list))
