def study_schedule(permanence_period, target_time):
    contador = 0
    for estudante in permanence_period:
        if (
            isinstance(estudante[0], int)
            and isinstance(estudante[1], int)
            and target_time is not None
        ):
            for hora in range(estudante[0], estudante[1] + 1):
                if hora == target_time:
                    contador += 1
        else:
            return None

    return contador


permanence_periods = [(4, None), ("0", 4)]
target_time = 4
print(study_schedule(permanence_periods, target_time))

# target_time = 4
# print(study_schedule(permanence_period, target_time))

# target_time = 3
# print(study_schedule(permanence_period, target_time))

# target_time = 2
# print(study_schedule(permanence_period, target_time))

# target_time = 1
# print(study_schedule(permanence_period, target_time))
