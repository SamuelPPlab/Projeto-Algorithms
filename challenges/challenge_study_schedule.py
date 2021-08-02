def study_schedule(permanence_period, target_time):

    count = 0
    if target_time is None:
        return None

    for t0, t1 in permanence_period:
        if type(t0) != int or type(t1) != int:
            return None
        if t0 <= target_time and target_time <= t1:
            count += 1

    return count
