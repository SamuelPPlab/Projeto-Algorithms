def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    number = 0

    for schedule in permanence_period:
        if None in schedule:
            return None
        if target_time in range(schedule[0], schedule[1]) or target_time in schedule:
            number += 1
    return number
