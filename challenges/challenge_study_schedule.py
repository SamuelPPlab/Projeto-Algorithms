def study_schedule(permanence_period, target_time):
    avaliable_students = 0
    try:
        for initial_time, final_time in permanence_period:
            if (initial_time <= target_time <= final_time):
                avaliable_students += 1
        return avaliable_students
    except TypeError:
        return None
