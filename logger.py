import logging

# Class ?
# Start init once
log_path = './'


def log_init():
    logging.basicConfig(filename=str(log_path) + 'tags_puller.log',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


def make_logs(sitename):
    logging.info('Sitename - ' + sitename)


if __name__ == '__main__':
    pass
