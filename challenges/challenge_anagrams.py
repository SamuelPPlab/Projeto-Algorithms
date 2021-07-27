def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    return sortString(first_string) == sortString(second_string)


def sortString(str):
    SHIFT = 32
    MAX_CHAR = 90
    result = ""
    charCount = [0 for i in range(MAX_CHAR)]
    for i in range(0, len(str), 1):
        charCount[ord(str[i]) - SHIFT] += 1
    for i in range(0, MAX_CHAR, 1):
        for j in range(0, charCount[i], 1):
            result += chr(SHIFT + i)

    return result
