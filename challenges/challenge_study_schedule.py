def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0
    for index in range(len(permanence_period)):
        p_period = permanence_period[index]
        if None in p_period:
            return None
        inicial_hour = p_period[0]
        end_hour = p_period[1]        
        if (inicial_hour <= target_time <= end_hour):
            counter += 1
    return counter
