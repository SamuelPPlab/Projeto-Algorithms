def isValid(entrie):
    for index in entrie:
        if None in index:
            return False
        else:
            return True


def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is not None and isValid(permanence_period):
        for item in permanence_period:
            if target_time >= item[0] and target_time <= item[1]:
                counter += 1
        return counter
    else:
        return None
