def is_anagram(first_string, second_string):
    return ''.join(sorted(list(first_string))) == \
      ''.join(sorted(list(second_string)))

