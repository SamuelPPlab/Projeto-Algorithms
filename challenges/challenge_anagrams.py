def gen_dict(chars):
    generate_dict = {}

    for char in chars:
        if char in generate_dict:
            generate_dict[char] += 1
        else:
            generate_dict[char] = 1

    return generate_dict


def is_anagram(first_string, second_string):
    first_string_chars = list(first_string)
    second_string_chars = list(second_string)

    first_string_dict = gen_dict(first_string_chars)
    second_string_dict = gen_dict(second_string_chars)

    return first_string_dict == second_string_dict
