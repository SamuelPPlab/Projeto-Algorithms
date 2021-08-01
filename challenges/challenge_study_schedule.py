def study_schedule(permanence_period, target_time):
    max_student_by_time = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                max_student_by_time += 1
    except TypeError:
        return None

    return max_student_by_time

