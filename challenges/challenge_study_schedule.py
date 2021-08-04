def study_schedule(permanence_periods, target_time):
    """Faça o código aqui."""
    students = 0
    try:
        for period in permanence_periods:
            if period[0] <= target_time <= period[1]:
                students += 1
    except TypeError:
        return None
    return students
