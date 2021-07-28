def study_schedule(permanence_period, target_time):
    # https://www.w3schools.com/python/ref_func_isinstance.asp

    result = 0
    if target_time is None:
        return None
    for periodo in permanence_period:
        if not isinstance(periodo[0], int) or not isinstance(periodo[1], int):
            return None
        elif target_time >= periodo[0] and target_time <= periodo[1]:
            result += 1
    return result
