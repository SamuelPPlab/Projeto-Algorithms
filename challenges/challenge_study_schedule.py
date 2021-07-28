def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time and target_time != 0:
        return None

    count = 0

    for x in permanence_period:
        if(x[0] is None or x[1] is None):
            return None
        if(target_time >= x[0] and target_time <= x[1]):
            count += 1
    return count
