def next_recursion(permanence_period, target_time):
    try:
        low_limit = permanence_period[-1][0]
        high_limit = permanence_period[-1][1]
        if low_limit <= target_time <= high_limit:
            students = 1
        else:
            students = 0
        return students + study_schedule(permanence_period[:-1],
                                         target_time)
    except TypeError:
        return None


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if len(permanence_period) == 1:
        if permanence_period[-1][0] <= target_time <= permanence_period[-1][1]:
            return 1
        else:
            return 0
    else:
        return next_recursion(permanence_period, target_time)
