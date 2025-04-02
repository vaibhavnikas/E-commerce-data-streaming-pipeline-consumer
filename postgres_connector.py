import psycopg2
import time


class PostgresDB():
    def __init__(self, host, port, db, user, pw):
        self.conn = psycopg2.connect(host=host, port=port, database=db, user=user, password=pw)
        self.cur = self.conn.cursor()

    def write(self, table:str, data:list):
        template = ','.join(['%s'] * len(data))
        insert_query = f"INSERT INTO {table} VALUES({template})"

        query_start_time = time.time()
        self.cur.execute(insert_query, data)
        query_end_time = time.time()
        query_execution_time = query_end_time - query_start_time
        print('Query executed in : ', query_execution_time)
        print(f"written to {table} : {data}")
        
        self.conn.commit()

    def writemany(self, table:str, data:list[tuple]):
        records_list_template = ','.join(['%s'] * len(data[0]))
        insert_query = f"INSERT INTO {table} VALUES({records_list_template})"

        query_start_time = time.time()
        self.cur.executemany(insert_query, data)
        query_end_time = time.time()
        query_execution_time = query_end_time - query_start_time
        print('Query executed in : ', query_execution_time)
        print(f"written to {table} : {data}")
        
        self.conn.commit()

    def execute(self, query:str):
        self.conn.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()

    def __del__(self):
        self.close()
