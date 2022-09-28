from modelos.users import Users
import utils as connection



class account:


    def __init__(self)-> None:
        pass

    def login(self, users):
        try:
            conn = connection.conexion()
            if self.__isvalidLogin(users) == True:
                query = " SELECT * FROM users WHERE __username = '{0}' ".format(users.getUsername())
                usuario = conn.run_query(query)

                if usuario != None:
                    if usuario.fetchall()[0][2] == users.getPassword():
                        return True
                    else:
                        return False

        except Exception as ex:
            print(ex)


    def creacion(self, users):
        try:
            conn = connection.conexion() # es una cnexion a la base de datos
            if self.__isvalidLogin(users) == True:
                query = " INSERT INTO users (__username, __password, __email) VALUES (?, ?, ?)"
                parameters = (users.getUsername(), users.getPassword(), users.getEmail())

                usuario = conn.run_query(query,parameters)

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
#usr = Users()
#usr.setUsername('sebas6')
#usr.setPassword('123456')
#usr.setEmail('sebas6@gmail.com')

# metodo que crea el objeto usuario en base de datos
#creacionUsuario = account()
#crear = creacionUsuario.creacion(usr)
#print(crear)