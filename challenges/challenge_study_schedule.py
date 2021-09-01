def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    students = 0

    for initial, final in permanence_period:
        if type(initial) != int or type(final) != int:
            return None
          
        if initial <= target_time <= final:
            students += 1

    return students
