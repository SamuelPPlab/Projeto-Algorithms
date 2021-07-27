def is_anagram(first_string, second_string):
    count = 0
    for letter in first_string:
        for letter_second in second_string:
            if letter_second == letter:
                count += 1
    if (
        count == len(first_string)
        and first_string != ""
        and second_string != ""
    ):
        return True
    return False
