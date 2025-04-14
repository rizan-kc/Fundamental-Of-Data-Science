'''
This program takes user input for the average temperature for each day of the week and stores it in a dictionary as a key 
value pair. Key = Day of the week and value = average temperature. 
'''
def get_daily_temps(mt):
    '''
    Asks the user too input the average temperature for each day of the week.
    
    dic: an empty dictionary to add average temperature for each corresponding days of the week. 
    Days are key while the average temperature is value.

    Returns the dictionary with days of the week as key and corresponding temperature as values.
    '''
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for day in days:
        avg_temp = int(input(f"Enter the average temperature for {day}: "))
        mt[day] = avg_temp
    return mt
dic = dict()
print(f"The dictionary containing corresponding days and average temperature of the week is:\n{get_daily_temps(dic)}")