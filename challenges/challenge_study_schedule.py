def is_not_type_int(entry):
    return (not type(entry[0]) == int) or (not type(entry[1]) == int)


def study_schedule(permanence_period, target_time):
    if (not target_time):
        return None

    count = 0

    for item in permanence_period:
        if is_not_type_int(item):
            return None
        if item[0] <= target_time <= item[1]:
            count += 1

    return count
