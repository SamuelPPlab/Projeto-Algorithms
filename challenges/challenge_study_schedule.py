def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    times = 0
    if target_time is None or type(target_time) != int:
        return None
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        if student[0] <= target_time <= student[1]:
            times += 1
    return times
