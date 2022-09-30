class Users:
    def __init__(self)-> None:
        pass

    __username = ""
    __password = ""
    __email = ""
    __date = ""
    __address = ""
    __userId = 0
    __message = ""

    # setters
    def setUsername(self, param):
        self.__username=param
    def setPassword(self, param):
        self.__password=param
    def setEmail(self, param):
        self.__email=param
    def setDate(self, param):
        self.__date=param
    def setAddress(self, param):
        self.__address=param
    def setUserid(self, param):
        self.__userid=param
    def setMessage(self, param):
        self.__message=param

    # metodos getter
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    def getDate(self):
        return self.__date
    def getAddress(self):
        return self.__address
    def getUserid(self):
        return self.__userid
    def setMessage(self):
        return self.__message

"""
u = users()
u.setUsername("brayan")
print(u.getUsername())
"""