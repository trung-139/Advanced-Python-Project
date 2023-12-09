import json
from datetime import datetime


class TimeFunction:
    def __init__(self):
        pass # init function is not used

    def time_split(self, time): 
        time_update = time[:2] + ":" + time[2:] # display format
        return time_update

    def str_to_datetime(self, time): # ?

        # time_update = self.time_split(time)
        time_obj = datetime.strptime(time, "%H:%M")
        return time_obj

    def time_calculation(self, time_from, time_to):

        time_from_obj = self.str_to_datetime(time_from)
        time_to_obj = self.str_to_datetime(time_to)

        total_time = list(str(time_to_obj - time_from_obj).split(":")) 

        hour = int(total_time[0])
        minute = int(total_time[1])

        new_total_time = round((hour + minute/60), 2) # event duration

        return new_total_time

    def date_validation(self, date):

        try:
            day, month, year = date.split("/") # check input syntax
        except ValueError:
            return False
        else:
            try:
                datetime(int(year), int(month), int(day)) # check data type
            except ValueError:
                return False
            else:
                return True

    def date_range_validation(self, date): # input date is valid if later than current date

        now = datetime.now()
        date = datetime.strptime(date, "%d/%m/%Y") ## date format

        if date < now:
            return False

        return True

    def time_format_validation(self, time): # check time format

        try:
            time_valid = datetime.strptime(time, "%H:%M")
        except ValueError:
            return False
        else:
            return True

    def time_range_validation(self, time_from, time_to): 

        time_valid_from = self.str_to_datetime("06:00")
        time_valid_to = self.str_to_datetime("21:30")
        time_from = self.str_to_datetime(time_from)
        time_to = self.str_to_datetime(time_to)

        if time_from < time_valid_from or time_to > time_valid_to:
            return False

        elif time_from >= time_to:
            return False

        return True

    def time_input_validation(self, time_from, time_to):

        time_from = self.str_to_datetime(time_from)
        time_to = self.str_to_datetime(time_to)

        if time_from > time_to:
            return False
        return True




