import data.usuarios as usuarios
conexionUsuarios = usuarios.Usuarios()
#print("Logueado?",conexionUsuarios.login("sebaaramyo123","rodriasdfsf"))
print(conexionUsuarios.obtenerTipoUsuario(1)[0][0])