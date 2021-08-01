def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    letters_first = first_string
    letters_second = second_string

    while len(letters_first) != 0:
        char = letters_first[0]

        letters_first = letters_first.replace(char, "")
        letters_second = letters_second.replace(char, "")

        if len(letters_first) != len(letters_second):
            return False

    return True
