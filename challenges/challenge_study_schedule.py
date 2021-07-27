def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for student in permanence_period:
            if student[0] <= target_time and student[1] >= target_time:
                count += 1
        return count
    except TypeError:
        return None


if __name__ == "__main__":
    permanence_period = [(1, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 5))
    print(study_schedule(permanence_period, 4))
    print(study_schedule(permanence_period, 3))
    print(study_schedule(permanence_period, 2))
    print(study_schedule(permanence_period, 1))
