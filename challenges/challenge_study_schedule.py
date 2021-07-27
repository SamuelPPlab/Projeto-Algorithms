# def study_schedule(permanence_period, target_time):
#     """ Faça o código aqui. """

# Segunda Tentativa
def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for start, end in permanence_period:
        if type(start) != int or type(end) != int:
            return None
        if start <= target_time <= end:
            count += 1
    return count

# Primeira tentativa
# def study_schedule(start_time, end_time, target_time):
#     count = 0
#     for index in range(len(start_time)):
#         if target_time in list(range(start_time[index], end_time[index] + 1))
#             count += 1
#     return count


# start_time = [2, 1, 2, 1, 4, 4]
# end_time = [2, 2, 3, 5, 5, 5]
# print(study_schedule(start_time, end_time, 4))
