def is_palindrome_iterative(word):
    if not word:
        return False
        
    wordcaracters = [char for char in word]
    reversecaracters = wordcaracters[::-1]
    if wordcaracters == reversecaracters:
        return True
    else:
        return False
