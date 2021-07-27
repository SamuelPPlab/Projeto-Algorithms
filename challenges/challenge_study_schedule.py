def study_schedule(permanence_period, target_time):
    contador = 0
    for estudante in permanence_period:
        start_time = estudante[0] or 0
        end_time = estudante[1]
        if (
            isinstance(start_time, int)
            and isinstance(end_time, int)
            and target_time is not None
        ):
            for hora in range(start_time, end_time + 1):
                if hora == target_time:
                    contador += 1
        else:
            return None

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
