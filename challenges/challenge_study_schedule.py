def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for time1, time2 in permanence_period:
            if (time1 <= target_time <= time2):
                students += 1
        return students
    except TypeError:
        return None
