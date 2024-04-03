import coneccionBBDD 

class Usuarios(coneccionBBDD.ConeccionBBDD):
    def obtenerUsuarios(self):
        datos = self.run_query("SELECT * FROM `usuario`")
        print(datos)
    def obtenerUsuario(self,id):
        datos = self.run_query(f"SELECT * from usuario  WHERE usuario.idUsuario = {str(id)}")
        print(datos)

    def obtenerUsuarioContrasenia(self,usuario):
        datos = self.run_query(f"SELECT usuario.idUsuario,usuario.contrasenia from usuario  WHERE usuario.usuario = '{str(usuario)}'")
        return datos
    
    def login(self,usuario,contrasenia):
        datosUsuario = self.obtenerUsuarioContrasenia(usuario)
        if len(datosUsuario) == 0:
            return False
        else:
            contraseniaReal = datosUsuario [0][1]
            if contraseniaReal == contrasenia:
                return True
            else:
                return False
