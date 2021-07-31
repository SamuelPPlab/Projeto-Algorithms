def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a


def particao(a, ini, fim):
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1
    # código acima foi retirado de https://pt.wikipedia.org/wiki/Quicksort


def is_anagram(first_string, second_string):
    sorted_first = quick_sort(list(first_string))
    sorted_second = quick_sort(list(second_string))
    if sorted_second == sorted_first:
        return True
    return False
