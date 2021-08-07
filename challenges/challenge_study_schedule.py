def study_schedule(permanence_period, target_time):
    """  Recebe:
            - permanence_period:
                - Tupla com horário de login e logout de estudantes do sistema;
            - target_time:
                - variável com horários a serem testados
        Retorna:
            - O número de estudantes estudando no mesmo horário
            - None se permanence_period for inválido"""

    active_students = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                active_students = active_students + 1
        return active_students
    except TypeError:
        return None
