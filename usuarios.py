import coneccionBBDD 
class Usuarios(coneccionBBDD.ConeccionBBDD):
    def obtenerUsuarios(self):
        datos = self.run_query("SELECT * FROM `usuario`")
        print(datos)
    def obtenerUsuario(self,id):
        pass
