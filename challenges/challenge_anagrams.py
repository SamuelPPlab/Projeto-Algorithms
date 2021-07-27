def removeCharacters(string, characters):
  retorno = list(string)
  for letra in characters:
        try:
            retorno.remove(letra)
        except Exception:
            return None
  return "".join(retorno)

def is_anagram(first_string, second_string):
    string_final = removeCharacters(first_string, second_string)
    print(string_final)
    if string_final != None and len(string_final) == 0: return True
    return False
