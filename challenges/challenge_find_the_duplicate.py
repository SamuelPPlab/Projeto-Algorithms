def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        if nums[0] < 0:
            return False
        return new_function(nums)
    except TypeError:
        return False
    except IndexError:
        return False


def new_function(nums):
    lista = sorted(nums)
    i = 0
    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            return lista[i]
        i += 1
    return False
