def study_schedule(permanence_period, target_time):
    number_students_in_interval = 0

    for start, end in permanence_period:
        if not (isinstance(start, int)
                and isinstance(end, int)
                and isinstance(target_time, int)):
            return None

        if start <= target_time <= end:
            number_students_in_interval += 1

    return number_students_in_interval


# if __name__ == '__main__':
#     permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
#     result = study_schedule(permanence_period, 4)
