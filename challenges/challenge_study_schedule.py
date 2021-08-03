def study_schedule(permanence_period, target_time):
    occurrences = 0
    try:
        for period in permanence_period:
            if (period[0] <= target_time <= period[1]):
                occurrences += 1
        return occurrences
    except TypeError:
        return None
