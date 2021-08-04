def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    better_hour = 0
    if (not target_time) or (target_time < 0):
        return None

    for start_time, end_time in permanence_period:
        if (not start_time or not end_time):
            return None
        if end_time >= target_time >= start_time:
            better_hour += 1
    return better_hour

# 1 - python3 -m pytest tests/test_study_schedule.py
# referencias
# Anderson Iarrocheski Stuber - Turma 6
# www.geeksforgeeks.org
# www.w3schools.com
# youtube
# https://pythoncafe.com.br/
# https://www.learnpython.org/
# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
# https://www.programiz.com/python-programming/examples/anagram
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
# https://www.kite.com/python/answers/how-to-check-for-duplicates-in-a-list-in-python
# https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
# http://pythontutor.com/visualize.html#mode=edit
# complexidade assintótica 
# 36 - algoritimo de ordenacao busca
