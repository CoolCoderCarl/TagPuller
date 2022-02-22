import datetime

today = datetime.date.today()

current_date_time = today.strftime("%Y.%m.%d")
current_year = int(current_date_time.split('.')[0])
current_month = int(current_date_time.split('.')[1])
current_day = int(current_date_time.split('.')[2])


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))


def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).date()


if __name__ == '__main__':
    pass