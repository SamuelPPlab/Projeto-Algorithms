def is_anagram(first_string, second_string):
    return ''.join(bubbleSort(list(first_string))) == \
      ''.join(bubbleSort(list(second_string)))


def bubbleSort(alist):
    alist = list(alist)
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return ''.join(alist)
