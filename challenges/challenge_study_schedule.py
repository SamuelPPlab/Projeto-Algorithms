def study_schedule(start_time, end_time, target_time):
    if not start_time or not target_time:
        return 0
    online_students = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            online_students += 1

    return online_students
