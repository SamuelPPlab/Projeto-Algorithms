def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for i in permanence_period:
            if i[0] <= target_time <= i[1]:
                count += 1
        return count
    except TypeError:
        return None
