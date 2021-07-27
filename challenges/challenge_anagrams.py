def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for first in first_string:
        for second in second_string:
            if first == second:
                return True
        return False


print(is_anagram('pedrra', 'pedraa'))