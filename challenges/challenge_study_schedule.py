def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if(target_time is None):
        return None
    period_in = 0
    for index in range(len(permanence_period)):
        if((permanence_period[index][0] is None) or
           (permanence_period[index][1] is None)):
            return None
        elif((target_time >= permanence_period[index][0]) and
             (target_time <= permanence_period[index][1])):
            period_in += 1
    return period_in

