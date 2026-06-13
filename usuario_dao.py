from conexion import obtener_conexion

class UsuarioDAO:

    def insertar_usuario(self, usuario):

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        consulta = """
            INSERT INTO usuarios (nombre, correo, edad)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            consulta,
            (usuario.nombre, usuario.correo, usuario.edad)
        )

        conexion.commit()
        cursor.close()
        conexion.close()