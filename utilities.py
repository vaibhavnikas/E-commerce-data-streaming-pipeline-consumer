import datetime


def get_date_dimensions(message):
    month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    dateinfo = message['date'].split('-')
    year = int(dateinfo[0])
    month = int(dateinfo[1])
    day = int(dateinfo[2])
    date = datetime.date(year, month, day)
    id = message['date']
    day_of_week = date.weekday() # 0: Monday, 1: Tuesday, . . . , 6: Sunday
    month_name = month_names[month]
    
    date_dimensions = [id, day, day_of_week, month, month_name, year]
    return date_dimensions
