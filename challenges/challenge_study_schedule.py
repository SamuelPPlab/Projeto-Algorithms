def study_schedule(permanence_period, target_time):
    times = 0
    if target_time is None or type(target_time) != int:
        return None
    for student in permanence_period:
        for teste in student:
            if type(teste) != int:
                return None
        if student[0] <= target_time <= student[1]:
            times += 1

    return times
