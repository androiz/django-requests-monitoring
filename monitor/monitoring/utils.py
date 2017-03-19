from datetime import datetime


def get_start_time():
    now = datetime.now()
    minute = str(now.minute)

    if len(minute) > 1:
        d = minute[0]
        u = '0' if int(minute[1]) > 5 else '1'
    else:
        d = '0'
        u = '0' if int(minute[0]) > 5 else '1'

    now.minute = int('{}{}'.format(d, u))
    return now


def get_time_range():
    pass


def charge_plot_data():
    pass
