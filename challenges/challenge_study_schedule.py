def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for student_period in permanence_period:
        if student_period[0] is None or student_period[1] is None:
            return None

        if student_period[0] <= target_time <= student_period[1]:
            count += 1

    return count
