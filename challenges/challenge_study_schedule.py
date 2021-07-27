def study_schedule(permanence_period, target_time):
    try:
        count = 0

        for entered, exited in permanence_period:
            if target_time >= int(entered) and target_time <= int(exited):
                count += 1

        return count
    except TypeError:

        return None
