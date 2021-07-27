def study_schedule(permanence_period, target_time):

    count = 0

    if target_time is None or type(target_time) != int:
        return None

    for aluno in permanence_period:
        if type(aluno[0]) != int or type(aluno[1]) != int:
            return None
        if aluno[0] <= target_time <= aluno[1]:
            count += 1

    return count
