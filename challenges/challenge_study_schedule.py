def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time:
        return None
    
    for i in range(0, len(permanence_period)):
        if type(permanence_period[i][0]) != int or type(permanence_period[i][1]) != int:
            return None
        if permanence_period[i][0] <= target_time <= permanence_period[i][1]:
            count += 1
    
    return count