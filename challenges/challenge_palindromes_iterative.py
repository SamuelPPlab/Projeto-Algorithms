def is_palindrome_iterative(word):
    # verifique se a palavra não é iterativa
    if len(word) <= 1:
        return False
    # itere através da palavra e verifique se a palavra é igual ao seu reverso
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            return False
    return True
