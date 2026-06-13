from usuario import Usuario
from usuario_dao import UsuarioDAO

# usuario = Usuario(
#     None,
#     "Juan Perez",
#     "juan@gmail.com",
#     25
# )

# usuario_dao = UsuarioDAO()
# usuario_dao.insertar_usuario(usuario)

# print("Usuario insertado correctamente")



usuario_dao = UsuarioDAO()

usuarios = usuario_dao.consultar_usuarios()

for usuario in usuarios:
    print(usuario)




# usuario_dao = UsuarioDAO()

# usuario = Usuario(
#     1,  # este es el id_usuario que ya existe en la bd
#     "Juan Actualizado",
#     "Actualizado@gmail.com",
#     30
# )

# usuario_dao.actualizar_usuario(usuario)

# print("Usuario actualizado correctamente")





# usuario_dao = UsuarioDAO()

# usuario_dao.eliminar_usuario(1)

# print("Usuario eliminado correctamente")