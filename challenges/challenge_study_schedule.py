def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    contador = 0
    for estudante in permanence_period:
        start_time = estudante[0]
        end_time = estudante[1]
        if type(start_time) != type(end_time) != "int":
            return None
        elif target_time >= start_time and target_time <= end_time:
            contador += 1

    return contador


# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target_time = 5
# print(study_schedule(permanence_periods, target_time))

# target_time = 4
# print(study_schedule(permanence_period, target_time))

# target_time = 3
# print(study_schedule(permanence_period, target_time))

# target_time = 2
# print(study_schedule(permanence_period, target_time))

# target_time = 1
# print(study_schedule(permanence_period, target_time))
