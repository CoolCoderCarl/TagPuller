import sqlite3


# From db
def get_data_from_db():
    """
    Get data from test.db database
    :return:
    """
    data = []
    with sqlite3.connect('test.db') as db:
        # db.row_factory = sqlite3.Row
        # cursor = db.cursor()
        query = """ 
                        SELECT * FROM test_table
                        """
        # cursor.execute(query)
        for row in db.cursor().execute(query):
            data = row
            # print(row)
    return data


def show_data_from_db():
    data = get_data_from_db()
    values = {}
    for row in data:
        print(row)


def test_show_data():
    with sqlite3.connect('test.db') as test_db:
        # cur = test_db.cursor()
        test_data = test_db.cursor().execute("""
                            SELECT id FROM test_table WHERE site_name='google'
                                """)
        for row in test_data:
            # print(row)
            # print(row)
            # print(test_list)
            return row[0]


if __name__ == "__main__":
    # print(get_data_from_db())
    # print(show_data_from_db())
    # print(test_show_data())
    pass
