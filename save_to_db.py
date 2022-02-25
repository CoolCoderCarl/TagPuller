import sqlite3

db_name = "test.db"


def is_db_exist() -> bool:
    """
    Check is db exist
    :return:
    """
    try:
        f = open(db_name)
        if f:
            return True
        else:
            return False
    except IOError:
        return False


def init_db():
    init_query = """
                    CREATE TABLE test_table
                    (domain TEXT, url_from_ui TEXT, timestamp INTEGER, tags_data TEXT)
                """

    with sqlite3.connect(db_name) as test_db:
        test_db.cursor().execute(init_query)


def is_db_empty():
    with sqlite3.connect(db_name) as test_db:
        query = """SELECT * FROM test_table"""
        test_db.cursor().execute(query)
        data = test_db.cursor().fetchall()
        if len(data) == 0:
            return True
        else:
            return False


def is_in_db(url_from_ui: str):
    """
    Check if data exist in db already
    :param url_from_ui:
    :return:
    """
    try:
        # if is_db_empty():
        #     return False
        # else:
            data = []
            with sqlite3.connect(db_name) as test_db:
                query = """
                        SELECT * FROM test_table WHERE url_from_ui = '%s'
                        """ % url_from_ui
                for row in test_db.cursor().execute(query):
                    data = row
                    if data:
                        return True
                    else:
                        return False
    except sqlite3.OperationalError as sqlerr:
        return sqlerr


def insert_into_db(domain: str, url_from_ui: str, timestamp: str, tags_data):
    """
    Insert into db information about tags which got from UI
    :param domain:
    :param url_from_ui:
    :param timestamp:
    :param tags_data:
    :return:
    """
    try:
        if is_in_db(url_from_ui):
            insert_data = [
                (domain,
                 url_from_ui,
                 timestamp,
                 tags_data)
            ]

            query = """
                        INSERT INTO test_table(domain, url_from_ui, timestamp, tags_data) VALUES (?,?,?,?);
                    """

            with sqlite3.connect(db_name) as test_db:
                test_db.cursor().executemany(query, insert_data)
        else:
            return True
    except sqlite3.OperationalError as sqlerr:
        return sqlerr


if __name__ == '__main__':
    # init_db()
    # print(is_in_db('www.google.com'))
    # print(is_db_empty())
    pass
