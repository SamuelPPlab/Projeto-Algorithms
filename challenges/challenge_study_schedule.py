def study_schedule(permanence_period, target_time):

    sum = 0

    if target_time is None or type(target_time) != int:
        return None

    for item in permanence_period:
        if type(item[0]) != int or type(item[1]) != int:
            return None
        if item[0] <= target_time and target_time <= item[1]:
            sum += 1
    return sum
