from collections import Counter

def is_anagram(first_string, second_string):
    return Counter(first_string) == Counter(second_string)
