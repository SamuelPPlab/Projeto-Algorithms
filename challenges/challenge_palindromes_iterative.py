def is_palindrome_iterative(word):
    if not word:
        return False
    if len(word) == 3 and word[0] == word[-1]:
        return True
    middle = len(word) // 2
    start = word[0:middle]
    end = word[(middle):len(word)]
    if len(word) % 2 == 1:
        end = end[1:]
    if start == end[::-1]:
        return True
    return False


# word = 'SOCOS'
# print(is_palindrome_iterative(word))
# word = 'ANNA'
# print(is_palindrome_iterative(word))
# word = 'REVIVER'
# print(is_palindrome_iterative(word))
