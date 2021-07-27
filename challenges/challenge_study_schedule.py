def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time:
        if target_time != 0:
            return None
    quantity = 0

    for item in permanence_period:
        if not (type(item[0]) == int) or not (type(item[1]) == int):
            return None
        else:
            if item[0] <= target_time <= item[1]:
                quantity += 1

    return quantity


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


print(study_schedule(permanence_period, 3))
