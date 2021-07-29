def study_schedule(permanence_period, target_time):
    count = 0

    if target_time is None or type(target_time) != int:
        return None

    for login, logout in permanence_period:
        if type(login) != int or type(logout) != int:
            return None
        if login <= target_time <= logout:
            count += 1

    return count
