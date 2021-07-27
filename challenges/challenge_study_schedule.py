def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for period in permanence_period:
            if target_time >= 0 and (
                target_time in range(period[0], period[1] + 1)
            ):
                counter += 1
    except TypeError:
        return None
    return counter
# referencia:
# https://pt.stackoverflow.com/questions/341085/como-validar-se-um-valor-%C3%A9-uma-tupla-possuindo-uma-string-e-um-inteiro
# try/except https://github.com/tryber/sd-07-project-algorithms/pull/3/files
