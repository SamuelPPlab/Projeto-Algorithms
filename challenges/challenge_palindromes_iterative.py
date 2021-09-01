def is_palindrome_iterative(word):
    if word == '':
        return False

    middle = len(word)//2
    initial = word[0:middle]
    final = word[middle:len(word)]

    if len(word) % 2 == 1:
        final = final[1:]
    if initial == final[::-1]:
        return True
    return False
