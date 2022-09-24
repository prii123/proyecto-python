from modelos.users import users
u = users()

print('--------------- welcome------------')
u.setUsername(input("por favor escriba su nombre: "))

print(u.getUsername())