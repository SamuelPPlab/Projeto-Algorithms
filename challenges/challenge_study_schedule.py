def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        counter = 0
        for time in permanence_period:
            if time[0] <= target_time and time[1] >= target_time:
                counter += 1
        return counter
    except TypeError:
        return None
