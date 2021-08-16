def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    number = 0

    for schedule in permanence_period:
        schedule_ok = target_time in schedule
        if None in schedule:
            return None
        if target_time in range(schedule[0], schedule[1]) or schedule_ok:
            number += 1
    return number
