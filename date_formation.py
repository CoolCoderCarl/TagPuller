import datetime

today = datetime.date.today()

current_date_time = today.strftime("%Y.%m.%d")


def get_y():
    return int(current_date_time.split('.')[0])


def get_m():
    return int(current_date_time.split('.')[1])


def get_d():
    return int(current_date_time.split('.')[2])


def get_timestamp(y, m, d):
    return datetime.datetime(y, m, d)


def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).date()


if __name__ == '__main__':
    # print(get_timestamp(get_y(), get_m(), get_d()))
    # print(type(get_timestamp(get_y(), get_m(), get_d())))
    pass
