def _is_present(student, target_time):
    return student[0] <= target_time <= student[1]


def study_schedule(permanence_period, target_time):
    try:
        return sum(_is_present(student, target_time)
                   for student in permanence_period)
    except TypeError:
        return None
