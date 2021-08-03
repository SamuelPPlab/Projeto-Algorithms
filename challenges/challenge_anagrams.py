from collections import Counter

def is_anagram(first_string, second_string):
    if Counter(first_string) == Counter(second_string):
        return True
    else:
        return False