def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for start, end in permanence_period:
        if start is None or end is None:
            return None
        if target_time >= start and target_time <= end:
            count += 1
    return count
