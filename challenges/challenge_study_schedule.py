def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """

    times = 0
    if target_time is None or type(target_time) != int:
        return None
    try:
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                times += 1
    except TypeError:
        return None
    return times
