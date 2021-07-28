def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        i = 0
        lista = nums.sort()
        while i < len(lista) - 1:
            if lista[i] == lista[i+1]:
                return lista[i]
            i += 1
    except TypeError:
        return False
