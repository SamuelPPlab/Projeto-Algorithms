def study_schedule(permanence_period, target_time):
    present_students = 0
    for period in permanence_period:
        if period[0] is None or period[1] is None or target_time is None:
            return None
        if period[0] <= target_time <= period[1]:
            present_students += 1
    return present_students
