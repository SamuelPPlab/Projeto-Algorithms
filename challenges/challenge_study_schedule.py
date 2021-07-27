def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for time in permanence_period:
        if time[0] is None or time[1] is None or type(time[0]) == str:
            return None
        if target_time >= time[0] and target_time <= time[1]:
            count += 1
    return count
