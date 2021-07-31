def is_anagram(first_string, second_string):
    if sorted(first_string) == sorted(second_string):
        print("true")
    elif (first_string == "") or (second_string == ""):
        print("false")
    else:
        print("false")


first_string = "pedra"
second_string = ""
is_anagram(first_string, second_string)
