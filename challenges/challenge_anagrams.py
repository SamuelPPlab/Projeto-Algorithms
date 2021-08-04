def is_anagram(first_string, second_string):
    if first_string == "":
        return False
    flaw = ""
    for i in first_string:
        for e in second_string:
            if i == e:
                flaw += i
    return isTrue(flaw, first_string)


def isTrue(flaw, first_string):
    if flaw == first_string:
        return True
    return False


# if __name__ == "__main__":
#    first_string = "pedra"
#    second_string = "perdaaa"
#    print(is_anagram(first_string, second_string))

########################################################
# def is_anagram(first_string, second_string):
#    if first_string == "":
#        return False
#    flaw = False
#    for i in range(len(first_string)):
#        for e in range(len(second_string)):
#            if first_string[i] == second_string[e]:
#                flaw = True
#    return flaw
