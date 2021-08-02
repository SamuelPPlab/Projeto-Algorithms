def study_schedule(permanence_period, target_time):
    if target_time != 0 and not target_time:
        return None
    count = 0
    for inicial, final in permanence_period:
        if (type(inicial) != int) or (type(final) != int):
            return None
        if (inicial <= target_time <= final):
            count += 1
    return count
