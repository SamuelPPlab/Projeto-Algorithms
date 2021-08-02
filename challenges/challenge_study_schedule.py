def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    students_quantity = 0

    for student in permanence_period:
        if not isinstance(student[0], int) or not isinstance(student[1], int):
            return None
        if target_time >= student[0] and target_time <= student[1]:
            students_quantity += 1
    return students_quantity
