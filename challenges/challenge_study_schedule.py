def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    number_of_online_students = 0
    for item in permanence_period:
        if type(item[0]) is not int or type(item[1]) is not int or type(target_time) is not int:
            return None
        if item[0] <= target_time and item[1] >= target_time:
            number_of_online_students += 1
    return number_of_online_students
