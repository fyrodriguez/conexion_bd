from usuario import Usuario
from usuario_dao import UsuarioDAO

usuario = Usuario(
    None,
    "Juan Perez",
    "juan@gmail.com",
    25
)

usuario_dao = UsuarioDAO()
usuario_dao.insertar_usuario(usuario)

print("Usuario insertado correctamente")