def study_schedule(period, target_time):
    count = 0

    if not target_time:
        return None

    for i in range(0, len(period)):
        if type(period[i][0]) != int or type(period[i][1]) != int:
            return None
        if period[i][0] <= target_time <= period[i][1]:
            count += 1

    return count
