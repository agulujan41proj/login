import data.coneccionBBDD as coneccionBBDD 

class Usuarios(coneccionBBDD.ConeccionBBDD):
    
    def obtenerUsuarios(self):
        datos = self.run_query("SELECT * FROM `usuario`")
        return datos
    def obtenerUsuario(self,id):
        datos = self.run_query(f"SELECT * from usuario  WHERE usuario.idUsuario = {str(id)}")
        return datos

    def obtenerUsuarioContrasenia(self,usuario):
        datos = self.run_query(f"SELECT usuario.idUsuario,usuario.contrasenia from usuario  WHERE usuario.usuario = '{str(usuario)}'")
        return datos
    
    def login(self,usuario,contrasenia):
        datosUsuario = self.obtenerUsuarioContrasenia(usuario)
        respuesta =[]
        if len(datosUsuario) == 0:
            respuesta.append(False)
            respuesta.append(["Usuario no encontrado"])
            
        else:
            contraseniaReal = datosUsuario [0][1]
            if contraseniaReal == contrasenia:
                respuesta.append(True)
                respuesta.append(datosUsuario[0])
                
            else:
                respuesta.append(False)
                respuesta.append(['Contraseña incorrecta'])

        return respuesta
    def obtenerTipoUsuario(self,idTipoUsuario):
        datos = self.run_query(f"SELECT tipousuario.descripcionUsuario from tipousuario where tipousuario.idTipoDeUsuario = {str(idTipoUsuario)}")
        return datos