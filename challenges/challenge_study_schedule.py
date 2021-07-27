def study_schedule(permanence_period, target_time):
    if (type(target_time) != int):
        return None
    counter = 0
    for schedule in permanence_period:
        if (type(schedule[0]) != int or type(schedule[1]) != int):
            return None
        if (schedule[0] <= target_time and schedule[1] >= target_time):
            counter += 1
    return counter
