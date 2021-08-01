def study_schedule(permanence_period, target_time):
    students_count = 0
    if target_time is None:
        return None
    for study_time in permanence_period:
        if(
            study_time[0] is None
            or study_time[1] is None
        ):
            return None
        elif (
            study_time[0] <= target_time
            and target_time <= study_time[1]
        ):
            students_count += 1

    return students_count
