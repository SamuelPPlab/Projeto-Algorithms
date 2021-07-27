from typing import Type


def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    online_students = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            online_students += 1

    return online_students
