def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for i in permanence_period:
        if(i[0] is None or i[1] is None):
            return None
        if(target_time >= i[0] and target_time <= i[1]):
            counter += 1
    return counter
