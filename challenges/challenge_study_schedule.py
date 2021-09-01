def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for index in permanence_period:
        if index[0] is None or index[1] is None or type(index[0]) == str:
            return None
        if target_time >= index[0] and target_time <= index[1]:
            count += 1
    return count
