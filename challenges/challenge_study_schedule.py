def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for element in permanence_period:
        if type(element[0]) != int or type(element[1]) != int:
            return None
        if element[0] <= target_time <= element[1]:
            counter += 1
    return counter
