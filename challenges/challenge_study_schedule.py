def study_schedule(permanence_period, target_time):
    counter = 0
    for time in permanence_period:
        try:
            if target_time >= time[0] and target_time <= time[1]:
                counter += 1
        except Exception:
            return None
    return counter
