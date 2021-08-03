def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for i, e in permanence_period:
        if isinstance(i, int) and isinstance(e, int):
            if i <= target_time <= e:
                counter += 1
        else:
            return None
    return counter


# if __name__ == "__main__":
#    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
#    print(study_schedule(permanence_period, 3))
