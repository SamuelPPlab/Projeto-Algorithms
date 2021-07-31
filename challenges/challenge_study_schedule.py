def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None or target_time == "0":
        return None

    for student in permanence_period:
        if (
            student[0] is None
            or student[0] == "0"
            or student[1] is None
            or student[1] == "0"
        ):
            return None
        if student[0] <= target_time and student[1] >= target_time:
            counter += 1
    return counter


permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_periods, 5))
