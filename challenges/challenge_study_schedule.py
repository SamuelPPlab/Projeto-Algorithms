def study_schedule(permanence_period, target_time):
    total_time = 0
    for aluno in permanence_period:
        try:
            if target_time >= aluno[0] and target_time <= aluno[1]:
                total_time = total_time + 1
        except:
            return None
    return total_time

# print(study_schedule([(2, 2), (1, 2), ("batata", 3), (1, 5), (4, 5), (4, 5)],3))
