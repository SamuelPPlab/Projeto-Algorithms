def is_anagram(first_string, second_string):
    word = ""
    if len(first_string) != len(second_string):
        return False
    for l1 in first_string:
        if l1 in word:
            return False
        elif l1 in second_string:
            word += l1
        else:
            return False
    return True


if __name__ == "__main__":
    first_string = "amor"
    second_string = "roma"
    print(is_anagram(first_string, second_string))
    # saída: True

    first_string = "pedra"
    second_string = "perda"
    print(is_anagram(first_string, second_string))
    # saída: True

    first_string = "pato"
    second_string = "tapo"
    print(is_anagram(first_string, second_string))
    # saída: True

    first_string = "coxinha"
    second_string = "empada"
    print(is_anagram(first_string, second_string))
    # saída: False

    first_string = "pedra"
    second_string = "pedro"
    print(is_anagram(first_string, second_string))
