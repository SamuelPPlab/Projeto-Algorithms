def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    online_students = 0
    for initial, final in permanence_period:
        if type(initial) != int or type(final) != int:
            return None
        if initial <= target_time <= final:
            online_students += 1
    return online_students
