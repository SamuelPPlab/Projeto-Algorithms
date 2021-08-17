def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # entendi observando o codeReview #58 - carlos8V
    students = 0
    try:
        for start_time, end_time in permanence_period:
            if(start_time <= target_time <= end_time):
                students += 1
        return students
    except TypeError:
        return None
