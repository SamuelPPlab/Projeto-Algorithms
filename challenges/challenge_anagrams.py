def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return Counter(first_string) == Counter(second_string)


def Counter(string):
    return {i: string.count(i) for i in set(string)}
