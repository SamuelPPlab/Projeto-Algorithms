def study_schedule(permanence_period, target_time):
    # permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    # target_time = 5
    if not target_time:
        return None

    cont = 0
    for element in permanence_period:
        if type(element[0]) != int or type(element[1]) != int:
            return None
        if element[0] <= target_time <= element[1]:
            cont += 1
    return cont
