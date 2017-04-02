from datetime import datetime


N_RANGES = 16


def get_start_time():
    now = datetime.now()
    minute = str(now.minute)

    if len(minute) > 1:
        d = minute[0]
        u = '0' if int(minute[1]) > 5 else '1'
    else:
        d = '0'
        u = '0' if int(minute[0]) > 5 else '1'

    start_minute = int('{}{}'.format(d, u))
    return now.replace(minute=start_minute)


def get_time_range():
    '''
    Return a list of tuples with len 16 and 2 times per tuble.
    i.e. : [(time0, time1),(time1, time2), ...(time15, time16)]
    '''

    pass


def charge_plot_data():
    '''
    Return a tuple with 2 lists. Each list contains 16 tuples with the x-coordinate time and the value.
    The first list get information about all requests for each time.
    The second list get information about post requests for each time.
    '''
    pass
