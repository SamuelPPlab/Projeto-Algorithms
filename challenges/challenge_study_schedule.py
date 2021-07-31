def study_schedule(permanence_period, target_time):
    teste = 0
    for hour in permanence_period:
        try:
            if hour[0] <= target_time and hour[1] >= target_time:
                teste = teste + 1
        except TypeError:
            return None
            break
    return teste
