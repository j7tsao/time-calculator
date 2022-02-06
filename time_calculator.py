# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

# Do not import any Python libraries. 
# Assume that the start times are valid times. 
# The minutes in the duration time will be a whole number less than 60, 
# but the hour can be any whole number.

def add_time(start, duration, start_day = None):
    new_time = str()
    semi = ':'  
    space = ' '
    comma = ', '
    hr_mins = 60
    day_mins = 60 * 24
    duration_mins = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    start_mins_passed = \
        (int(start.split()[0].split(':')[0]) * 60 \
            + int(start.split()[0].split(':')[1]) + 720, \
            int(start.split()[0].split(':')[0]) * 60 \
                + int(start.split()[0].split(':')[1]))\
                [start.split()[1] == 'AM']

    # mins left away from 12AM on the start day
    start_mins_left = day_mins - start_mins_passed

    # the start time plus duration in mins
    total_mins = start_mins_passed + duration_mins

    # dictionary for weekdays
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # start day index
    if start_day:
        start_day_index = list(weekdays.values()).index(start_day.capitalize())

    # ending on the same day
    if duration_mins < start_mins_left:
        end_min = total_mins % hr_mins

        if ( total_mins // hr_mins) < 12:
            end_hr = total_mins // hr_mins
            ampm = 'AM'
        elif ( total_mins // hr_mins) == 12:
            end_hr = 12
            ampm = 'PM'
        else:
            end_hr = total_mins // hr_mins - 12
            ampm = 'PM'
        
        new_time = \
            (str(end_hr) + semi + str(end_min).zfill(2) + space + ampm, \
                str(end_hr) + semi + str(end_min).zfill(2) + \
                    space + ampm + comma + str(start_day).capitalize())\
                        [start_day != None]
    
    # ending on the next day
    elif duration_mins >= start_mins_left \
        and duration_mins < start_mins_left + day_mins:
        
        nextdayMsg = " (next day)"
        end_min = total_mins % hr_mins       

        if ( total_mins - day_mins ) // hr_mins < 12:
            if ( total_mins - day_mins ) // hr_mins == 0:
                end_hr = 12
            else:
                end_hr = ( total_mins - day_mins ) // hr_mins
            ampm = 'AM'
        elif ( total_mins - day_mins ) // hr_mins == 12:
            end_hr = 12
            ampm = 'PM'
        else:
            end_hr = ( total_mins - day_mins ) // hr_mins - 12
            ampm = 'PM'

        if start_day:
            end_day_index = 0 if start_day_index == 6 else start_day_index + 1 
            end_day = weekdays.get(end_day_index, 'The index does not exist.')
            new_time = str(end_hr) + semi + str(end_min).zfill(2) \
                    + space + ampm + comma + str(end_day).capitalize() \
                        + nextdayMsg
        else:
            new_time = str(end_hr) + semi + str(end_min).zfill(2) \
                + space + ampm + nextdayMsg
        
    # ending beyond the next day
    elif duration_mins > start_mins_left \
        and duration_mins > start_mins_left + day_mins:

        end_min = total_mins % hr_mins
        numOfDay = total_mins // day_mins
        weekdayMsg = f" ({ numOfDay } days later)"

        if ( total_mins - numOfDay * day_mins) // hr_mins < 12:
            if ( total_mins - numOfDay * day_mins) // hr_mins == 0:
                end_hr = 12
            else:
                end_hr = ( total_mins - numOfDay * day_mins) // hr_mins
            ampm = 'AM'
        elif ( total_mins - numOfDay * day_mins) // hr_mins == 12:
            end_hr = 12
            ampm = 'PM'
        else:
            end_hr = ( total_mins - numOfDay * day_mins) // hr_mins - 12
            ampm = 'PM'
        
        if start_day:
            end_day_index = (numOfDay - 1) % 7 if start_day_index == 6 \
                else (start_day_index + numOfDay) % 7
            end_day = weekdays.get(end_day_index, 'The index does not exist.')
            new_time = str(end_hr) + semi + str(end_min).zfill(2) \
                    + space + ampm + comma + str(end_day).capitalize() \
                        + weekdayMsg
        else:
            new_time = str(end_hr)+ semi + str(end_min).zfill(2) \
                + space + ampm + weekdayMsg

    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
print(add_time("8:16 PM", "466:02", "tuesday"))