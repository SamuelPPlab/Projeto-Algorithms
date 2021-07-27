def find_duplicate(nums):
    """ Faça o código aqui. """
    if type(nums) is list:
        i = 0
        lista = nums.sort()
        while i < len(lista) - 1:
            if lista[i] == lista[i+1]:
                return lista[i]
    return False
