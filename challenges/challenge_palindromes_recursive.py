def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    return word == reverse(word)


def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + list[0]


# def is_palindrome_recursive(word, low_index, high_index):
#     if len(word) < 2 and word != "":
#         return True
#     if word == '':
#         return False
#     else:
#         if word[low_index] == word[high_index]:
#             word = word[1:-1]
#             return is_palindrome_recursive(word, low_index, len(word) - 1)
#         else:
#             return False


# print(is_palindrome_recursive("", 0, 0))
