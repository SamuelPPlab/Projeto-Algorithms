def study_schedule(permanence_period, target_time):
    estudantes = 0
    try:
        for periodo in permanence_period:
            if periodo[0] <= target_time <= periodo[1]:
                estudantes += 1
    except TypeError:
        return None
    return estudantes
