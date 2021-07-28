
def is_palindrome_iterative(word):
    if not word:
        return False
    array_length = len(word)//2
    count = len(word)
    count2 = 0
    array = list(word)

    for _ in range(array_length):
        count -= 1
        if(array[count] != array[count2]):
            return False
        count2 += 1
    return True
