def is_palindrome_recursive(word, low_index=0, high_index=0):
    print(word)
    if not word:
        return False
    if word[0] != word[-1]:
        return False
    if len(word) <= 3:
        print("returning true")
        return True
    is_palindrome_recursive(word[1:-1])

is_palindrome_recursive("SOCOS")