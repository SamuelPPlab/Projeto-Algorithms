def study_schedule(permanence_period, target_time):
    all_times = []
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if None in period or target_time is None:
            return None
        diff_time = period[1] - period[0]
        if diff_time == 0:
            all_times.append(period[1])
        elif diff_time == 1:
            all_times.append(period[0])
            all_times.append(period[1])
        else:
            interm = 0
            while interm < period[1]:
                interm += 1
                all_times.append(interm)

    return all_times.count(target_time)
