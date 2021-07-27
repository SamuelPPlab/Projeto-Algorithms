def study_schedule(permanence_period, target_time):
    counter = 0
    START = 0
    END = 1

    if target_time is None:
        return None

    for _index, period in enumerate(permanence_period):
        if not isinstance(period[START], int) or not isinstance(
            period[END], int
        ):
            return None
        if period[START] <= target_time <= period[END]:
            counter += 1

    return counter
