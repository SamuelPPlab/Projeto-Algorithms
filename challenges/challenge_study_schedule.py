def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for timeInterval in permanence_period:
        entry, exit = timeInterval
        if type(entry) is not int or type(exit) is not int:
            return None
        if timeInterval[0] <= target_time <= timeInterval[1]:
            counter += 1
    return counter
