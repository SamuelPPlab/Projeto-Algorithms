def is_palindrome_iterative(word):
    if len(word) == 1:
        return True
    if not word:
        return False
    reversed_list = []
    for item in list(word):
        reversed_list.insert(0, item)
    if word == ''.join(reversed_list):
        return True
    else:
        return False
