def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or target_time < 0:
        return None

    counter = 0
    for element in permanence_period:
        if not isinstance(element[0], int) or not isinstance(element[1], int):
            return None

        if element[0] <= target_time <= element[1]:
            counter += 1

    return counter


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, 2))
