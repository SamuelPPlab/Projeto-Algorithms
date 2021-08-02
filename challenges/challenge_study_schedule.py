def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for tuplas in permanence_period:
        if tuplas[0] is None or tuplas[1] is None:
            return None

        if target_time >= tuplas[0] and target_time <= tuplas[1]:
            count += 1

    return count
