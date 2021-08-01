def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time:
        return None
    c = 0
    for i in permanence_period:
        if not i[0] or not i[1]:
            return None
        if i[0] <= target_time <= i[1]:
            c += 1
    return c
