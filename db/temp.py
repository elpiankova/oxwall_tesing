import pymysql


def _our_hash(password):
    d = {
        "pass": "592490bd0faa5a417a1aa7cf7aca26e8551a1b2d3238c618a9d17d1bfc4bbbef",
        "test": "a2b84e6c176c01e1aacd3312469e5ac732978f6534af33290882f5aa32be572c",
        "secret": "74210d690a28b4372ca86ff249c472975d860a537d19f0f551cd2c7d908222ea"
    }
    return d[password]


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mysql',
                             db='oxwall1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

user = {
        "username": "test123",
        "password": "test",
        "real_name": "Tester",
        "email": "test123@test.com",
        "gender": 1
    }

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = f"""INSERT INTO `ow_base_user` (`email`, `password`, `username`, `emailVerify`, `joinIp`, `accountType`)
    #               VALUES ('{user["email"]}','{_our_hash(user["password"])}', '{user["username"]}',
    #               1, '2130706433', '290365aadde35a97f11207ca7e4279cc')"""
    #     cursor.execute(sql)
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    username = "admin"
    cursor = connection.cursor()
    # Read a single record
    sql = "SELECT `id`, `email`, `username`, `password` FROM `ow_base_user`"
    cursor.execute(sql)
    connection.commit()
    result1 = cursor.fetchall()
    print(result1)
finally:
    connection.close()
