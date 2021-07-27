def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """

    result = 0
    if target_time is None:
        return None
    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None
        elif target_time >= i[0] and target_time <= i[1]:
            result += 1
    return result
