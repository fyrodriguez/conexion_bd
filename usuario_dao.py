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

    def consultar_usuarios(self):

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        consulta = "SELECT * FROM usuarios"

        cursor.execute(consulta)

        usuarios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return usuarios
    
    def actualizar_usuario(self, usuario):

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        consulta = """
            UPDATE usuarios
            SET nombre = %s,
                correo = %s,
                edad = %s
            WHERE id_usuario = %s
        """

        cursor.execute(
            consulta,
            (usuario.nombre, usuario.correo, usuario.edad, usuario.id_usuario)
        )

        conexion.commit()
        cursor.close()
        conexion.close()