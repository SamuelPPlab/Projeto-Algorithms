def study_schedule(permanence_period, target_time):
    try:
        students_online = 0
        for student_period in permanence_period:
            if (
                student_period[0] <= target_time
                and student_period[1] >= target_time
            ):
                students_online += 1
        return students_online
    except TypeError:
        return None
