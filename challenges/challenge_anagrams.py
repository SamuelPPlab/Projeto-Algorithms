def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    letters_first = first_string
    letters_second = second_string

    for letter in first_string:
        letters_first = letters_first.replace(letter, "")
        letters_second = letters_second.replace(letter, "")

        if len(letters_first) != len(letters_second):
            return False

    return True
