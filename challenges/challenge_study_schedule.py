def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    all_times = 0
    for time_in, time_out in permanence_period:
        if type(time_in) != int or type(time_out) != int:
            return None

        if time_in <= target_time and target_time <= time_out:
            all_times += 1
        # referência: Vitor Rodrigues

    return all_times
