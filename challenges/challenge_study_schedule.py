def study_schedule(start_time, end_time, target_time):
    if len(start_time) + len(end_time) + target_time == 0:
        return 0
    student_counter = 0
    for student in range(len(start_time)):
        if end_time[student] >= target_time >= start_time[student]:
            student_counter += 1
    return student_counter
