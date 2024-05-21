import data.coneccionBBDD as coneccionBBDD 

class Turno(coneccionBBDD.ConeccionBBDD):
    def obtenerProfesionales(self):
        datos = self.run_query("SELECT * FROM usuario WHERE usuario.idTipoUsuario = 3;")
        return datos 
    def obtenerPacientes(self):
        datos = self.run_query("SELECT * FROM usuario WHERE usuario.idTipoUsuario = 4;")
        return datos 
    def insertarTurno(self,idPaciente,idEmpleado,fecha,hora):
        self.run_query(f"INSERT INTO `turnos` (`idTurno`, `idPaciente`, `idProfesional`, `fecha`, `hora`) VALUES (NULL, '{idPaciente}', '{idEmpleado}', '{fecha}', '{hora}');")
        #INSERT INTO `turnos` (`idTurno`, `idPaciente`, `idProfesional`, `fecha`, `hora`) VALUES (NULL, '9', '8', '2024-06-09', '10:00:00');

    def obtenerTodosLosTurnos(self):
        datos = self.run_query("SELECT * FROM `turnos`")
        return datos