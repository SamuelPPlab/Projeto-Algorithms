def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    length_arr = len(permanence_period)
    if (target_time is None):
        return None

    students_online = 0
    for index in range(length_arr):
        if (None in permanence_period[index]):
            return None
        if((target_time >= permanence_period[index][0]) and
           (target_time <= permanence_period[index][1])):
            students_online += 1
    return students_online
