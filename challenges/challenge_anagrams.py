def is_anagram(first_string, second_string):
    word1 = list(first_string)
    word2 = list(second_string)
    if len(word1) != len(word2):
        return False
    else:
        for letter in word1:
            if letter in word2:
                word2.remove(letter)
        return len(word2) == 0
