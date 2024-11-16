import sqlite3
from config import db_name


class Database:
    def __init__(self) -> None:
        self.db_name = db_name
        
        self.conn = sqlite3.connect(f'{self.db_name}.db')
        self.cursor = self.conn.cursor()
        



    def GenerateTable(self, table_name, **kwargs):
        try:
            values = ''
            rows = list(kwargs.keys())
            params = list(kwargs.values())

            for i in range(len(list(rows))):
                values += f"{rows[i]} {params[i]},"
            else:
                values = values[:-1]

            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS "{table_name}" (
                id INTEGER PRIMARY KEY,
                {values}
            );
            ''')

            self.conn.commit()
            
            return True

        except Exception as e:
            print(f'[sql GenerateTable] {e}')
            return False
    

    def GetOne(self, data, table_name, find_param, find_value):
        try:
            query = f'SELECT {data} FROM {table_name} WHERE {find_param} = {find_value}'

            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.conn.commit()

            return result

        except sqlite3.Error as e:
            print(f"[sql GetOne] {e}")
            return False


    def GetAll(self, data, table_name, find_param, find_value):
        try:
            query = f'SELECT {data} FROM {table_name} WHERE {find_param} = {find_value}'

            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.conn.commit()
            
            return results

        except sqlite3.Error as e:
            print(f"[sql GetAll] {e}")
            return False


    def AddRow(self, table_name, **kwargs):
        '''
        True если все гуд
        False если не все гуд
        '''
        try:
            values = '?,'*(len(kwargs)-1) + '?'

            command = f''' 
            INSERT INTO "{table_name}" ({", ".join(list(kwargs.keys()))})
            VALUES ({values})
            '''

            self.cursor.execute(command, tuple(kwargs.values()))
            self.conn.commit()

            return True
        
        except Exception as e:
            print('[sql AddRow]', e)
            return False
