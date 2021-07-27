from collections import Counter


def verifica(period):
    return isinstance(period[0], int) and isinstance(period[1], int)


def total_list_range(permanence_period):
    total_list = []
    for tuple_time in permanence_period:
        total_list += list(range(tuple_time[0], tuple_time[1] + 1))
    return total_list


def study_schedule(permanence_period, target_time):
    todas_tuplas_validas = True
    if not isinstance(target_time, int):
        return None

    for period in permanence_period:
        if not verifica(period):
            todas_tuplas_validas = False
            break

    if not todas_tuplas_validas:
        return None
 
    total_list = total_list_range(permanence_period)
    best_period = Counter(total_list)
    return best_period[target_time]

# https://pt.stackoverflow.com/questions/341085/como-validar-se-um-valor-%C3%A9-uma-tupla-possuindo-uma-string-e-um-inteiro
