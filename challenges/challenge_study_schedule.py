def valid(target_time):
    if not target_time:
        if target_time != 0:
            return True


def study_schedule(permanence_period, target_time):
    if valid(target_time):
        return None
    quantity = 0
    for item in permanence_period:
        if not (type(item[0]) == int) or not (type(item[1]) == int):
            return None
        else:
            if item[0] <= target_time <= item[1]:
                quantity += 1
    return quantity
