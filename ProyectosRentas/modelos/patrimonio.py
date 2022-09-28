class Patrimonio:

    def __init__(self) -> None:
        pass

    __id = 0
    __idUsuario = 0
    __nombreActivo = ""
    __valor = 0

# metodos getter
    def getId(self):
        return self.__id
    def getIdUsuario(self):
        return self.__idUsuario
    def getNombreActivo(self):
        return self.__nombreActivo
    def getValor(self):
        return self.__valor

# metodos setter
    def setId(self, param):
        self.__id=param
    def setIdUsuario(self, param):
        self.__idUsuario=param
    def setNombreActivo(self, param):
        self.__nombreActivo=param
    def setValor(self, param):
        self.__valor=param

"""
pt = Patrimonio()
pt.setId(2)
pt.setIdUsuario(3)
pt.setNombreActivo('cuenta ahorro bancolombia')
pt.setValor(300000)

print(pt.getId())
print(pt.getIdUsuario())
print(pt.getNombreActivo())
print(pt.getValor())
"""