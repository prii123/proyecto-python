class Pasivos:

    def __init__(self) -> None:
        pass

    __id = 0
    __idUsuario = 0
    __nombrePasivo = ""
    __valor = 0

# metodos getter
    def getId(self):
        return self.__id
    def getIdUsuario(self):
        return self.__idUsuario
    def getNombrePasivo(self):
        return self.__nombrePasivo
    def getValor(self):
        return self.__valor

# metodos setter
    def setId(self, param):
        self.__id=param
    def setIdUsuario(self, param):
        self.__idUsuario=param
    def setNombrePasivo(self, param):
        self.__nombrePasivo=param
    def setValor(self, param):
        self.__valor=param

"""
pt = Pasivos()
pt.setId(2)
pt.setIdUsuario(3)
pt.setNombrePasivo('Trajeta Credito bancolombia')
pt.setValor(500000)

print(pt.getId())
print(pt.getIdUsuario())
print(pt.getNombrePasivo())
print(pt.getValor())
"""