def study_schedule(permanence_period, target_time):
    counter = 0
    for item in permanence_period:
        try:
            if target_time >= item[0] and target_time <= item[1]:
                counter += 1
        except TypeError:
            return None
    return counter


# if __name__ == "__main__":
#     permanence_periods = [(0, "0"), (4, 4), (1, 3), (3, 4), (2, 5)]
#     print(study_schedule(permanence_periods, 5))
