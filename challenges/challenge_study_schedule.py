from collections import Counter


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    get_periods = get_hours(permanence_period)
    if get_periods is None:
        return get_periods

    contador = Counter(get_periods)
    return contador[target_time]


def get_hours(permanence_period):
    desmontando_tuplas = []
    for hour in permanence_period:
        # https://www.geeksforgeeks.org/python-type-function/
        if type(hour[0]) is not int or type(hour[1]) is not int:
            return None
        if (hour[1] - hour[0]) > 1:
            hour = get_interval(hour)
        if hour[0] == hour[1]:
            hour = same_values(hour)
        desmontando_tuplas = append_tupla(hour, desmontando_tuplas)
    return desmontando_tuplas


def get_interval(hour):
    for i in range(hour[0], hour[1]):
        if i > hour[0]:
            # https://www.it-swarm-es.com/es/python/como-agregar-valor-una-tupla/972119161/
            hour = hour + (i,)
    return hour


def append_tupla(hour, desmontando_tuplas):
    for countHour in hour:
        desmontando_tuplas.append(countHour)
    return desmontando_tuplas


def same_values(hour):
    # https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-12.php
    my_list = []
    became_list = list(hour)
    remove_item = became_list.pop(1)
    my_list.append(remove_item)
    became_tuple = tuple(my_list)
    return became_tuple
