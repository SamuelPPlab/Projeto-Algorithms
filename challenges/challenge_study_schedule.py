def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if target_time is None:
        return None
    for period in permanence_period:
        lower = period[0]
        upper = period[1]
        if type(lower) != type(upper) != 'int':
            return None
        elif target_time >= lower and target_time <= upper:
            counter += 1
    return counter
