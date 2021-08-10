def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # number = 0
    # if target_time is None:
    #     return None

    # for student in permanence_period:
    #     if student[0] <= target_time <= student[1]:
    #         number += 1
    # return number

    number = 0
    try:
        for start, end in permanence_period:
            if start <= target_time <= end:
                number += 1
        return number
    except TypeError:
        return None
