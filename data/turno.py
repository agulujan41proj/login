import data.coneccionBBDD as coneccionBBDD 

class Turno(coneccionBBDD.ConeccionBBDD):
    def obtenerProfesionales(self):
        datos = self.run_query("SELECT * FROM usuario WHERE usuario.idTipoUsuario = 3;")
        return datos 
    def obtenerPacientes(self):
        datos = self.run_query("SELECT * FROM usuario WHERE usuario.idTipoUsuario = 4;")
        return datos 