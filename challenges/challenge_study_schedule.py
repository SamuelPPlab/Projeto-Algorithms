def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for index, element in permanence_period:
            if (index <= target_time and target_time <= element):
                counter += 1
        return counter
    except TypeError:
        return None

# referencia Carol Bezerra
