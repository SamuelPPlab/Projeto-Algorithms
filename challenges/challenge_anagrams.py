def is_anagram(first_string, second_string):
    if first_string == "":
        return False
    flaw = False
    for i in range(len(first_string)):
        for e in range(len(second_string)):
            if first_string[i] == second_string[e]:
                flaw = True
    return flaw


if __name__ == "__main__":
    first_string = "pedra"
    second_string = "perdaaa"
    print(is_anagram(first_string, second_string))


# def is_anagram(first_string, second_string):
#    if first_string == "":
#        return False
#    flaw = ""
#    for i in first_string:
#        for e in second_string:
#            if i == e:
#                flaw += i
#    if flaw == first_string:
#        return True
#    else:
#        return False

######################################################
# def is_anagram(first_string, second_string):
#    if first_string == "":
#        return False
#    flaw = False
#    for i in range(len(first_string)):
#        for e in range(len(second_string)):
#            if first_string[i] == second_string[e]:
#                flaw = True
#    return flaw

# def is_anagram(first_string, second_string):
#    """ Faça o código aqui. """
#    reverse = ''.join(list(second_string)[::-1])
#    if len(first_string) != len(second_string):
#        return False
#    if first_string == second_string:
#        return True
#    if first_string != reverse:
#        return True
#    else:
#        return False
#
