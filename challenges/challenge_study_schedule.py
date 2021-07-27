def study_schedule(permanence_period, target_time):
    cont = 0

    if (
        target_time is None
    ):
        return None

    for index in range(len(permanence_period)):
        if (
            not isinstance(permanence_period[index][0], int) or
            not isinstance(permanence_period[index][1], int)
            # not all(isinstance(value, int) for value in permanence_period[index]) or
        ):
            return None

        if (
            permanence_period[index][0] <= target_time and
            permanence_period[index][1] >= target_time
        ):
            cont += 1

    return cont
