import sys
import os

rutaRaiz = os.path.dirname(os.path.abspath(__file__)).split('ProyectosRentas')[0]
sys.path.append(rutaRaiz + r'ProyectosRentas\modelos')
sys.path.append(rutaRaiz + r'ProyectosRentas\utils')
"""
from ..modelos.users import Users
from ..utils import utils as connection
"""

import users
import utils as connection

class Account:
    def __init__(self)-> None:
        pass

    def login(self, users):
        try:
            if self.__isvalidLogin(users) == True:
                query = " SELECT * FROM users WHERE __username = ?"
                usuario = connection.run_query(query,users.getUsername())
                if usuario != None:
                    if usuario.fetchall()[0][2] == users.getPassword():
                        return True
                    else:
                        return False
        except Exception as ex:
            print(ex)


    def creacion(self, users):
        try:
            if self.__isvalidLogin(users) == True:
                query = " INSERT INTO users (__username, __password, __email) VALUES (?, ?, ?)"
                parameters = (users.getUsername(), users.getPassword(), users.getEmail())
                usuario = connection.run_query(query,parameters)
                if usuario != None:
                    return True
        except Exception as ex:
            print(ex)



    def __isvalidLogin(self, users):
        if users.getUsername() != "" and users.getPassword() != "":
            return True
        return False

    def __isAuthentic(users):
        if users.getUsername()=="NIIT" and users.getPassword()=="pass":
            return True
        return False

    def __Authorize(users):
        users.setMessage(users.getUsername()+" is logged In ....")





# creacion  de un objeto usuario
usr = users.Users()
usr.setUsername('brayan')
usr.setPassword('123')
#usr.setEmail('sebas6@gmail.com')
"""
print(usr.getUsername())
print(usr.getPassword())
"""
#metodo que crea el objeto usuario en base de datos
#creacionUsuario = Account()
#crear = creacionUsuario.login(usr)
#print(crear)


query = 'SELECT * FROM users WHERE __username = ?'
usuario = connection.run_query(query, usr.getUsername())
print(usuario)


"""
query = 'SELECT * FROM users'
print(connection.run_query(query).fetchall())
"""

