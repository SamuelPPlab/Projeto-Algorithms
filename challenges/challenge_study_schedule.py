def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    for student in permanence_period:
        try:
            if target_time >= student[0] and target_time <= student[1]:
                count += 1
        except TypeError:
            return None
    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
