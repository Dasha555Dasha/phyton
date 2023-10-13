from datetime import datetime

def string_to_datetime(date_string):
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime_obj = datetime.strptime(date_string, date_format)
    return datetime_obj

date_string = "2022-01-01 12:00:00"
datetime_obj = string_to_datetime(date_string)
print(datetime_obj)
