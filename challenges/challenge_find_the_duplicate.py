def find_duplicate(nums):
    if not nums or nums != int:
        return False
    # encontre o número de elementos
    n = len(nums)
    # armazenar os elementos
    s = set()
    # iterar através da matriz
    for i in range(n):
        # verifique se o elemento está presente
        if nums[i] in s:
            return nums[i]
        # adicione o elemento
        s.add(nums[i])
    return -1
