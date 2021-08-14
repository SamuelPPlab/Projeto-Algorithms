def study_schedule(permanence_period, target_time):
    output = 0
    for student in permanence_period:
        start_time = student[0]
        end_time = student[1]
        if start_time <= target_time and end_time >= target_time:
            output = output + 1
    return output
