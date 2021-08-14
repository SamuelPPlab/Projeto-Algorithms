def study_schedule(permanence_period, target_time):
    output = 0
    if target_time is not None:
        for student in permanence_period:
            start_time = student[0] if type(student[0]) == int else None
            end_time = student[1] if type(student[0]) == int else None
            if start_time is not None and end_time is not None:
                if start_time <= target_time and end_time >= target_time:
                    output = output + 1 if type(output) == int else None
            else:
                output = None
        return output
    else:
        return None
