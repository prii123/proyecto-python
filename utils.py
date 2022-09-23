import sqlite3

class funcionesUtiles():
    db_name = 'database.db'

    def __init__(self):
        pass

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def validation(self, valor1, valor2):
        return len(valor1) != 0 and len(valor2)