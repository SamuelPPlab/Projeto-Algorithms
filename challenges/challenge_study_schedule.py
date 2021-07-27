def study_schedule(permanence_period, target_time):
    counter = 0
    for i in range(len(permanence_period)):
        try:
            if (
                permanence_period[i][0] <= target_time
                and permanence_period[i][1] >= target_time
            ):
                counter += 1
        except TypeError:
            return None

    return counter
