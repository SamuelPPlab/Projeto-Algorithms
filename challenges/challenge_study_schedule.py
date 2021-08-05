def study_schedule(permanence_period, target_time):
    students_present = 0

    try:

        for period in permanence_period:
            arrive_hour = period[0]
            depart_hour = period[1]

            if arrive_hour <= target_time <= depart_hour:
                students_present += 1

    except TypeError:
        return None
    return students_present
