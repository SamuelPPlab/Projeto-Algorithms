def is_anagram(first_string, second_string):
    palavra1 = list(first_string)
    palavra2 = list(second_string)
    if len(palavra1) != len(palavra2):
        return False
    else:
        for letra in palavra1:
            if letra in palavra2:
                palavra2.remove(letra)
        return len(palavra2) == 0
