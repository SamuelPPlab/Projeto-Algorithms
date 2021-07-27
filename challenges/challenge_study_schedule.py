def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """

    times = 0
    try:
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                times += 1
    except TypeError:
        return None 
    return times
