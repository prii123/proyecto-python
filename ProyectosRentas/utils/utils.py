import sqlite3
import sys
import os
rutaRaiz = os.path.dirname(os.path.abspath(__file__)).split('ProyectosRentas')[0]


def run_query(query, parameters=()):
    db_name = rutaRaiz + r'ProyectosRentas\db\database.db'
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    except Exception as ex:
        print(ex)
    conn.close()

def validation(valor1, valor2):
    return len(valor1) != 0 and len(valor2) != 0



#print(run_query('SELECT * FROM users').fetchall())