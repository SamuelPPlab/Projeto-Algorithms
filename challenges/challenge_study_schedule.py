def study_schedule(start_time, end_time, target_time):
    result = 0
    for x1, x2 in zip(start_time, end_time):
        if target_time >= x1 and target_time <= x2:
            result += 1
    return result
