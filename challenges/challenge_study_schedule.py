def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None

    for student_time in permanence_period:
        if type(student_time[0]) != int or type(student_time[1]) != int:
            return None
        if target_time >= student_time[0] and target_time <= student_time[1]:
            counter += 1

    return counter
