from datetime import datetime, timedelta

from .models import LogEntry

N_RANGES = 16


def get_start_time():
    now = datetime.now()
    minute = str(now.minute)

    if len(minute) > 1:
        d = minute[0]
        u = '0' if int(minute[1]) < 5 else '5'
    else:
        d = '0'
        u = '0' if int(minute[1]) < 5 else '5'

    start_minute = int('{}{}'.format(d, u))
    print(start_minute, d, u)
    return now.replace(minute=(start_minute+5) % 60, second=0)


def get_time_range():
    '''
    Return a list of tuples with len 16 and 2 times per tuble.
    i.e. : [(time0, time1),(time1, time2), ...(time15, time16)]
    '''
    result = []
    time0 = get_start_time()
    for i in range(0, N_RANGES):
        time1 = time0 - timedelta(minutes=5)
        result.append((time1, time0))
        time0 = time1
    result.reverse()
    return result


def charge_plot_data():
    '''
    Return a tuple with 2 lists. Each list contains 16 tuples with the x-coordinate time and the value.
    The first list get information about all requests for each time.
    The second list get information about post requests for each time.
    '''
    data1 = []
    data2 = []

    ranges = get_time_range()

    for range in ranges:
        n = LogEntry.objects.filter(created_at__gt=range[0], created_at__lte=range[1]).count()
        data1.append(range[1].strftime("%H:%M"))
        data2.append(n)
    return data1, data2
