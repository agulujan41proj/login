import data.coneccionBBDD as coneccionBDDD

class Empleados(coneccionBDDD.ConeccionBBDD):
    def obtenerEmpleados(self):
        datos = self.run_query("SELECT usuario.idUsuario,usuario.apellido,usuario.nombre,empleados.rol,usuario.dni,usuario.cuit,usuario.fechaNacimiento,usuario.direccion,usuario.email, usuario.ultimoAcceso,usuario.habilitado from empleados INNER JOIN usuario ON empleados.idUsuario = usuario.idUsuario;")
        return datos
    
    def actualizarRol(self,idUsuario,rol):

        self.run_query(f"UPDATE `empleados` SET `rol` = '{rol}' WHERE `empleados`.`idUsuario` = {str(idUsuario)}");