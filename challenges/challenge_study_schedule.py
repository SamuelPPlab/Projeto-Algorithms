def study_schedule(permanence_period, target_time):
    if not start_time or not target_time:
        return 0
    quantity = 0
    for item in range(len(start_time)):
        if start_time[item] <= target_time <= end_time[item]:
            quantity += 1
    return quantity
