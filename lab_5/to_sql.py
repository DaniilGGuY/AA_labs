import psycopg2
from os import listdir
from os.path import isfile, join

class Lab:
    def __init__(self):
        print("Подключение к базе данных...")
        self.__conn = psycopg2.connect(dbname="postgres",
                                      user="postgres",
                                      password="postgres123",
                                      host="localhost")
        print("Подключение выполнено успешно.")
        self.__cursor = self.__conn.cursor()
        print("Готов к работе.")

    def __del__(self):
        print("Отключение от базы данных...")
        self.__cursor.close()
        self.__conn.close()
        print("Отключено.\nВыход...")

    def create_db_request(self):
        sql_cr_schema = """create schema if not exists aalab;"""
        self.__cursor.execute(sql_cr_schema)

        sql_cr_table = """
            create table if not exists aalab.parse (
                id integer,
                issue_id integer,
                url text,
                title text,
                author text,
                ingredients json,
                steps json
            );
            alter table aalab.parse add constraint id_pk primary key(id);"""
        self.__cursor.execute(sql_cr_table)

        files = [join("data_json", f) for f in listdir("data_json") if isfile(join("data_json", f))]
        for i in files:
            print(i)
            sql_add_file = "create temp table tmp ( tmp json );\n" + \
                f"copy tmp from 'D:\Study\AA_labs\lab_5\\{i}';\n" + \
                "insert into aalab.parse\n" + \
                "select (json_populate_record(null::aalab.parse, json_array_elements(tmp))).* from tmp;\n" + \
                "drop table tmp;"
            self.__cursor.execute(sql_add_file)
        self.__conn.commit()

db = Lab()
db.create_db_request()
