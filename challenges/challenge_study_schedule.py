def study_schedule(start_time, end_time, target_time):
    counter = 0

    if not target_time:
        return 0

    for start_time_inter, stop_time_iter in zip(start_time, end_time):
        if start_time_inter <= target_time <= stop_time_iter:
            counter += 1

    return counter
