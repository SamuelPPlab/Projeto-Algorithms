def selection_sort(word):
    for i in range(0, len(word) - 1):
        minIndex = i
        for j in range(i+1, len(word)):
            if(word[j] < word[minIndex]):
                minIndex = j
        if minIndex != i:
            word[minIndex], word[i] = word[i], word[minIndex]
    return word

# referencia:
# https://www.google.com/search?q=how+to+implement+algorithm+selection+sort+in+python&ei=ZGUFYZ6UHrfc1sQPnpqPuA0&oq=how+to+implement+algorithm+selection+sort+in+pyhti&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCEQChCgAToHCAAQRxCwAzoFCAAQkQI6BAgAEEM6BQgAEIAEOgsILhCABBDHARCjAjoFCC4QgAQ6BggAEBYQHjoECAAQDToGCAAQDRAeOggIABAWEAoQHjoKCCEQFhAKEB0QHjoICAAQCBANEB46CAghEBYQHRAeOgUIIRCgAToECCEQFUoECEEYAFC8owFY1MACYNzGAmgDcAJ4AIAB5wSIAY8pkgEIMC4zOC41LTGYAQCgAQHIAQjAAQE&sclient=gws-wiz#kpvalbx=_smUFYYeiEsjQ1sQPqvOuwAw18


def is_anagram(first_string, second_string):
    first_string = selection_sort(list(first_string))
    second_string = selection_sort(list(second_string))
    return first_string == second_string
