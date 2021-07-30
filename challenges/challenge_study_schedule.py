def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if type(target_time) != int:
        return None
    active_students = 0
    for initial, final in permanence_period:
        if type(initial) != int or type(final) != int:
            return None
        if initial <= target_time <= final:
            active_students += 1
    return active_students