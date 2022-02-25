import sqlite3


# From db
def get_data_from_db(domain: str):
    """
    Show data which got from DB
    :return:
    """
    with sqlite3.connect("test.db") as test_db:
        # cur = test_db.cursor()
        query = """
                        SELECT * FROM test_table WHERE domain='%s'
                """ % domain
        test_data = test_db.cursor().execute(query)
        for row in test_data:
            # print(row)
            # print(row)
            # print(test_list)
            return row[-1]


if __name__ == "__main__":
    # get_data_from_db('google')
    pass
