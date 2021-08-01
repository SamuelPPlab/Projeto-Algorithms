def study_schedule(permanence_period, target_time):
    target_time_rate = 0

    if target_time is None:
        return None

    for period in permanence_period:
        if (period[0] is None or period[1] is None):
            return None

        if int(period[0]) <= int(target_time) <= int(period[1]):
            target_time_rate += 1

    return target_time_rate
