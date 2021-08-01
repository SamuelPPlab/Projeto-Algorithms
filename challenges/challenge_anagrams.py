def listSorted(string):
    my_list = []
    for i in range(len(string)):
        for key, value in enumerate(my_list):
            if string[i] < value:
                my_list.insert(key, string[i])
                break
        else:
            my_list.append(string[i])
    return my_list


def is_anagram(first_string, second_string):
    if listSorted(first_string) == listSorted(second_string):
        return True
    else: 
        return False

