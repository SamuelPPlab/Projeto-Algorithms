def study_schedule(start_time, end_time, target_time):
    if not target_time or not start_time or not end_time:
        return 0
    counter = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time and end_time[i] >= target_time:
            counter += 1
    return counter
