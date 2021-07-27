def is_anagram(first_string, second_string):
    teste = list(second_string)
    for letra in first_string:
        try:
            teste.remove(letra)
        except:
            return False
    if len(teste) == 0:
        return True
    return False
