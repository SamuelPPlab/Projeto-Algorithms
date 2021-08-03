def study_schedule(permanence_period, target_time):
    contador = 0
    if not target_time:
        return None
    for entrada, saida in permanence_period:
        if not entrada or not saida:
            return None
        if entrada <= target_time <= saida:
            contador += 1
    return contador