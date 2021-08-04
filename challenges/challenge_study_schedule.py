def study_schedule(permanence_period, target_time):
    # if not target_time:
    #     return None
    # # permanence_period é um [entrada, saída), (entrada, saída)]
    counter = 0
    try:
        for login, logout in permanence_period:
            if login <= target_time <= logout:
                counter = counter + 1
        return counter
    except TypeError:
        return None
