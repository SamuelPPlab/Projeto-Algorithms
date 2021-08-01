def study_schedule(permanence_period, target_time):
    try:
        initial_counter = 0
        for time in permanence_period:
            if time[0] <= target_time and time[1] >= target_time:
                initial_counter += 1
        return initial_counter
    except TypeError:
        return None
