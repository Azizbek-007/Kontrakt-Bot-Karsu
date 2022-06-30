from sqlite3 import Error
import sqlite3
from time import ctime


def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE "USERS" (
	"id"	INTEGER,
	"user_id"	INTEGER,
	"t_id"	INTEGER,
	"reg_dat"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);'''

    post_sql_query(users_query)


def register_user(user, t_id=None):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user}'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, t_id, reg_dat) VALUES ' \
                             f'({user}, {t_id}, "{ctime()}");'
        post_sql_query(insert_to_db_query)
        return user_check_data
    else:
        return False


def rege_student(t_id, user=None):
    sql = f"SELECT * FROM payment WHERE st_id = {t_id}"
    data = post_sql_query(sql)
    if data != []:
        register_user(user, t_id)
        return data
    else:
        return False

def student_info(t_id):
    sql = f"SELECT * FROM payment WHERE st_id = {t_id}"
    data = post_sql_query(sql)
    return data

create_tables()



