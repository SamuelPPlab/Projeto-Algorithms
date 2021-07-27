def study_schedule(permanence_period, target_time):
    cont = 0

    if target_time is None:
        return None

    for start, stop in permanence_period:
        if (
            not isinstance(start, int) or
            not isinstance(stop, int)
        ):
            return None

        if start <= target_time <= stop:
            cont += 1

    return cont
