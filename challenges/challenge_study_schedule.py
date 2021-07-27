def study_schedule(permanence_period, target_time):
    try:
        total_list = []
        if not isinstance(target_time, int):
            return None

        for period in permanence_period:
            total_list += list(range(period[0], period[1] + 1))
    except TypeError:
        return None
    return total_list.count(target_time)
# referencia:
# https://pt.stackoverflow.com/questions/341085/como-validar-se-um-valor-%C3%A9-uma-tupla-possuindo-uma-string-e-um-inteiro
# try/except https://github.com/tryber/sd-07-project-algorithms/pull/3/files
