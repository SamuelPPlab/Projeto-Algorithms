def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None

    for start_time, end_time in permanence_period:
        if type(start_time) != int or type(end_time) != int:
            return None
        if start_time <= target_time <= end_time:
            counter += 1

    return counter
