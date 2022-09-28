from utils import conexion
from modelos.users import Users
#u = Users()

aa = conexion()

print('--------------- welcome------------')
#u.setUsername(str(input("por favor escriba su nombre: ")))
#u.setPassword(str(input("por favor escriba su password: ")))
#u.setEmail(str(input("por favor escriba su email: ")))

query = 'INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?)'
parameters = ('brayan', '123', 'prii@gmail.com', '2022-01-01', 'cl 57 28 20')
datos = aa.run_query(query, parameters)
print(datos)


#print(u.getUsername())
#print(u.getPassword())
#print(u.getEmail())