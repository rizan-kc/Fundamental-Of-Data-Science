'''
This program uses an empty dictionary to store the days and the corresponding average temperature for that day.
The day is stored as key while average temperature is stored as value.
'''
def add_daily_temp(rec,day,temp):
    '''
    Adds the average daily temperature to the dictionary, if the day is not 
    present in the dictionary.

    Parameters:
    rec: Dictionary with days as key and temperature as value.
    day: The day of the week.
    temp: The average temperature of the day.

    Returns an updated dictionary with new temperature if day was not already 
    present in the dictionary.
    '''

    if day not in rec:
        rec[day] = temp
    return rec

dic = dict()
print(add_daily_temp(dic,"Monday",40))
print(add_daily_temp(dic,"Tuesday",36))
print(add_daily_temp(dic,"Monday",45))
