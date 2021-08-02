def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None

    counter = 0
    in_time = 0
    out_time = 1

    for schedule in permanence_period:
        if schedule[in_time] is None or schedule[out_time] is None:
            return None

        if schedule[in_time] <= target_time <= schedule[out_time]:
            counter += 1

    return counter
