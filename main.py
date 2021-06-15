import sqlalchemy
import requests_CREATE
import requests_INSERT
import requests_SELECT

if __name__ == '__main__':
    db = 'postgresql://tester:1234@localhost:5432/test_base'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    requests_CREATE.create_table(connection)
    requests_INSERT.insert_data(connection)
    requests_SELECT.select_db(connection)
